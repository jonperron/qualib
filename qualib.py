#!/usr/bin/env python
# -*- coding : utf-8 -*-

"""
Quali'B core.
"""

import time

from cassandra.cluster import Cluster
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table

from qualib.datarake import SNCFDataRake
from qualib.models import TrainStop

__author__ = "Jonathan Perron"
__version__ = "2.0"
__maintainer__ = "Jonathan Perron"
__email__ = "contact@jonathanperron.fr"
__repo__ = "https://github.com/jonperron/qualib"

KEYSPACE = "qualib"

def main():
    while True:
        SNCFDataRake().retrieve_missions_sncf()
        time.sleep(300) # waiting 5 minutes   
        
if __name__ == '__main__':
    # Setup Cassandra
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()

    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS %s
        WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }
        """ % KEYSPACE)

    connection.setup(['127.0.0.1'], KEYSPACE, protocol_version=3)
    sync_table(TrainStop)
    
    main()