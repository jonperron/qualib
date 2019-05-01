# /usr/bin/python3
# -*- coding : utf-8 -*-

"""
Quali'B classes to retrieve data
"""
__author__ = "Jonathan Perron"
__version__ = "1.0"
__maintainer__ = "Jonathan Perron"
__email__ = "contact@jonathanperron.fr"
__repo__ = "https://github.com/jonperron/qualib"

import json
import logging
import os

import requests

from logging.handlers import RotatingFileHandler
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from qualib.models import TrainStop

# Conf logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
file_handler = RotatingFileHandler(os.path.join(os.path.dirname(os.path.realpath(__file__)), "qualib.log"), 'a', 5000000, 1)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler) 


class DataRake:
    """
    Abstract class used to retrieve data from provider APIs
    """
    def __init__(self, *args, **kwargs)-> None:
        self.stations = None
        self.get_stops()

    def get_stations(self) -> None:
        """
        Get stations from configuration/train_stations.json file
        """
        stations = []
        with open("configuration/train_stations.json") as json_file:
            train_stations = json.load(json_file)
            with station in train_stations:
                stop.append({
                    "gtfs": station.get("GTFS"),
                    "name": station.get("Nom"),
                    "longitude": station.get("Longitude"),
                    "latitude": station.get("Latitude"),
                    "sncfID": station.get("SncfId"),
                })

        self.stations = stations


class SNCFDataRake(DataRake):
    """
    Class retrieving data from SNCF APIs.
    """
    def __init__(self, *args, **kwargs) -> None:
        self.login = None
        self.password = None
        self.get_credentials()
        super().__init__(*args, **kwargs)

    def get_credentials(self) -> None:
        """
        Get auth credentials from configuration/sncf_credentials.json file
        """
        with open("configuration/sncf_credentials.json") as json_file:
            credentials = json.load(json_file)
            self.login = credentials["SNCFAPILogin"]
            self.password = credentials["SNCFAPIPassword"]

    def retrieve_missions_sncf(self) -> None:
        """
        Retrieve data from SNCF APIs
        """
        # Filter stations
        sncf_stations = tuple(x for x in self.stations if x["sncfID"] is not None)

        # Create requests session
        session = requests.Session()
        session.auth = (self.login, self.password)
        retry = Retry(
            total=5,
            read=5,
            connect=5,
            backoff_factor=0.3,
            status_forcelist=(500, 502, 504),
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        # Init beautifulsoup
        soup = BeautifulSoup(r.content, "lxml-xml")

        # Read data from APIs
        for station in sncf_stations:
            try:
                r = session.get('http://api.transilien.com/gare/{0}/depart/'.format(station["gtfs"]))
                next_stops = soup.find_all("train")
                for stop in next_stops:
                    mission = TrainStop.create(
                        station=station["name"],
                        code=stop.find("miss"),
                        network="SNCF",
                        date=datetime.strptime(mission.find("date").text,"%d/%m/%Y %H:%M"),
                    )
            except Exception as e:
                logging.error("%s", str(e))
