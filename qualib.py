#!/usr/bin/env python
# -*- coding : utf-8 -*-

"""
Quali'B core.
"""

from datetime import datetime
import folium
import time
import logging
from logging.handlers import RotatingFileHandler
import os
import pandas as pd
import zeep

from qualib.conf import SNCF_API_LOGIN,SNCF_API_PASSWORD
from qualib.classes import Mission, Gares
from qualib.delays import get_missions_ratp, get_missions_sncf, get_delays
from qualib.mapping import color, icon, icon_color

__author__ = "Jonathan Perron"
__version__ = "0.2"
__maintainer__ = "Jonathan Perron"
__email__ = "contact@jonathanperron.fr"
__repo__ = "https://github.com/jonperron/qualib"

def main():
    logger.info("Initialization")
    # SOAP Client
    client = zeep.Client(wsdl = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Wsiv.wsdl"))
    
    # results dataframe
    traffic = pd.DataFrame(columns=['Gare','Longitude','Latitude','Trafic'])
    
    # Define the line object for SOAP
    line_type = client.get_type('ns0:Line')
    line = line_type(id = 'RB')
    
    # Define the station object for SOAP
    station_type = client.get_type('ns0:Station')
    station = station_type(line = line)
    
    # Define the direction object for SOAP
    direction_type = client.get_type('ns0:Direction')
    direction = direction_type(sens = '*')
    
    # Get all stations from the line
    logger.info("Getting stations list from RATP APIs.")
    stations = client.service.getStations(station = station)
    
    # List all stations
    list_stations = []
    for i in range(0,len(stations['stations'])):
        list_stations.append((stations['stations'][i]['id'], stations['stations'][i]['name']))
    
    logger.info("Starting Quali'B")
    while True:
        try:
            tic = datetime.now()
            # Get all missions status
            get_missions_tasks = []
            for station in Gares.LISTE_GARES:
                if station[4]:
                    get_missions_tasks.append((station,get_missions_sncf(station,SNCF_API_LOGIN,SNCF_API_PASSWORD)))
                else:
                    get_missions_tasks.append((station,get_missions_ratp(station,client,line,direction,station_type)))
    
            # Reorganize the delays by station
            stations_delays = dict()
            for item in get_missions_tasks:
                station_name = item[0]
                if item[1]:
                    for train in item[1]:
                        if station_name in stations_delays:
                            stations_delays[station_name].append(train[1])
                        else:
                            stations_delays[station_name] = [train[1]]
                else:
                    stations_delays[station_name] = [None]    
            
            logging.info(stations_delays)
            # Determine the traffic in each station based on the number of missions' statuses
            i = 0
            for key, value in stations_delays.items():
                status = max(set(value), key = value.count)
                if status is None: #redraw if None
                    value = [x for x in value if x is not None]
                    try:
                        status = max(set(value), key = value.count)
                    except ValueError:
                        status = None
            
                traffic.loc[i] = [
                    key[1],
                    [x[3] for x in Gares.LISTE_GARES if x[1] == key[1]][0],
                    [x[2] for x in Gares.LISTE_GARES if x[1] == key[1]][0],
                    status
                ]
                i +=1
            
            # Map generation !
            map=folium.Map(location=[traffic['Latitude'].mean(),traffic['Longitude'].mean()],zoom_start=11)
            
            for name,lat,lon,traf in zip(traffic['Gare'],traffic['Latitude'],traffic['Longitude'],traffic['Trafic']):
                map.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(icon=icon(traf),color=color(traf),icon_color=icon_color(traf))))
                map.save(outfile='webserver/public/test.html')
    
            toc = datetime.now()
            logging.info("Map generated in " + str((tic - toc).seconds) + " seconds.")
            time.sleep(300) # waiting 5 minutes   
        except Exception as e:
            logging.exception("message")
            break
        
if __name__ == '__main__':
    # Conf logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
    file_handler = RotatingFileHandler(os.path.join(os.path.dirname(os.path.realpath(__file__)), "qualib.log"), 'a', 5000000, 1)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)    
    main()