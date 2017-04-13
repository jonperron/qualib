#!/usr/bin/env python
# -*- coding : utf-8 -*-

"""
Quali'B tests.
"""
from datetime import datetime
import os
import sqlite3
import unittest

from qualib.classes import Mission
from qualib.delays import get_delays

__author__ = "Jonathan Perron"
__version__ = "0.2"
__maintainer__ = "Jonathan Perron"
__email__ = "contact@jonathanperron.fr"
__repo__ = "https://github.com/jonperron/qualib"

class QualiBTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def _mock_mission_ratp(self):
        mission = Mission()
        mission.create_mission('Orsay Ville','ISOL','RATP',True)
        return mission

    def _mock_mission_sncf(self):
        mission = Mission()
        mission.create_mission('Parc des Expositions','PDRI','SNCF',True)
        # creating date directly, otherwise would require bs4.element.Tag
        mission.date = datetime(2017,4,12,16,55)
        return mission

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_database_connection(self):
        conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'horaires.db'))
        c = conn.cursor()
        c.execute('SELECT * FROM theorie')
        self.assertNotEqual(len(c.fetchall()), 0)

    def test_parsing_date_ratp(self):
        mission = self._mock_mission_ratp()
        mission.get_mission_date({'stationsDates' : ['201703301700']})
        self.assertEqual(mission.date,datetime(2017,3,30,17,00))

    def test_delay_ratp(self):
        mission = self._mock_mission_ratp()
        mission.get_mission_date({'stationsDates' : ['201703301700']})
        delay = get_delays(mission)
        self.assertEqual(delay,"Normal")

    def test_delay_sncf(self):
        mission = self._mock_mission_sncf()
        delay = get_delays(mission)
        self.assertEqual(delay,"Normal")

if __name__ == '__main__':
    unittest.main()