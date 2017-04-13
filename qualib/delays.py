# /usr/bin/python3
# -*- coding : utf-8 -*-

"""
Quali'B main functions used to determine train delays !
"""

__author__ = "Jonathan Perron"
__version__ = "0.2"
__maintainer__ = "Jonathan Perron"
__email__ = "contact@jonathanperron.fr"
__repo__ = "https://github.com/jonperron/qualib"

from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
import os
import requests
import sqlite3

from .classes import Mission,Gares

def get_missions_ratp(station,client,line,direction,station_type):
    """
    Effectue la requete SOAP pour chacune des stations sur l'API open data de la RATP
    """
    station_ = station_type(name = station[1], line = line)
    next_stops = client.service.getMissionsNext(station = station_, direction = direction)
    delays = []
    for stop in next_stops['missions']:
        mission = Mission()
        mission.create_mission(station[1],stop['code'],"RATP",stop['stationsStops'])
        mission.get_mission_date(stop)
        delays.append((station,get_delays(mission)))
    
    return delays

def get_missions_sncf(station,SNCF_API_LOGIN,SNCF_API_PASSWORD):
    """
    Effectue la requete pour chaque station sur l'API open data Transilien de la SNCF
    """
    station = ([x[4] for x in Gares.LISTE_GARES if x[1] == station[1]][0],station[1])
    r = requests.get('http://api.transilien.com/gare/' + station[0] +'/depart/', auth=(SNCF_API_LOGIN, SNCF_API_PASSWORD))
    soup = BeautifulSoup(r.content, "lxml-xml")
    next_stops = soup.find_all("train")
    delays = []
    for stop in next_stops:
        mission = Mission()
        mission.create_mission(station[1],stop.find("miss").text,"SNCF",True)
        mission.get_mission_date(stop)
        delays.append((station,get_delays(mission)))

    return delays

def get_delays(mission):
    """
    Analyse le résultat de la requête et indique si le train est en retard ou non.
    """
    if mission.date and mission.stops and abs(datetime.now() - datetime.combine(date.today(),mission.date.time())) <= timedelta(minutes=30):
        # Execute SQL request - c is coming from main code
        conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'horaires.db'))
        c = conn.cursor()
        request = c.execute("SELECT * FROM theorie WHERE Mission = ? AND Gare = ? AND JOUR = ?",[mission.code,mission.station,mission.date.strftime("%A")]).fetchall()
        # Times are not stored in SQLite DB, so we need to transform them to make any comparisons. Otherwise, we would need to make the transfo beforehand !
        request_items = []
        for item in request:
            if int(item[3][0:2]) < 24: # We exclude hours above 24 !
                horaire = datetime.strptime(item[3],"%H:%M:%S").time()
            else:
                correctif = str(int(item[3][0:2]) - 24) + item[3][2:]
                horaire = datetime.strptime(correctif,"%H:%M:%S").time()
            request_items.append((item[0],horaire))

        # Determine closest expected mission
        # http://stackoverflow.com/questions/5259882/subtract-two-times-in-python
        if request_items:
            delta_position = min(range(len(request_items)), key=lambda i: abs(datetime.combine(date.today(),mission.date.time()) - datetime.combine(date.today(),request_items[i][1])))
            delta_minutes = datetime.combine(date.today(),mission.date.time()) - datetime.combine(date.today(),request_items[delta_position][1])
        
            if timedelta(seconds=0) <= abs(delta_minutes) < timedelta(seconds=120):
                return "Normal"
            elif timedelta(seconds=120) < abs(delta_minutes) <= timedelta(seconds=300):
                return "Retard leger"
            elif timedelta(seconds=300) < abs(delta_minutes) <= timedelta(seconds=600):
                return "Retard important"
            else:
                return "Supprime"
        else:
            return None
    else:
        return None
