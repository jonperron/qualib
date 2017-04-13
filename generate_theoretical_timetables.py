# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Starting from the data from the SNCF API, generates the database containing all the theoretical timetables.
"""

__author__ = "Jonathan Perron"
__version__ = "1.0"
__maintainer__ = "Jonathan Perron"
__email__ = "contact@jonathanperron.fr"
__repo__ = "https://github.com/jonperron/qualib"

import pandas as pd
import sqlite3
import os

conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'horaires.db'))
c = conn.cursor()
c.execute('CREATE TABLE theorie(ID INT PRIMARY KEY NOT NULL, Mission CHAR(16) NOT NULL, Gare CHAR(64) NOT NULL, Horaire TEXT NOT NULL, Jour CHAR(16) NOT NULL, Debut CHAR(16) NOT NULL, Fin CHAR(16) NOT NULL)')

# import from all files
agency = pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'horaires/agency.txt'))
calendar = pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'horaires/calendar.txt'))
calendar_dates = pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'horaires/calendar_dates.txt'))
routes = pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'horaires/routes.txt'))
stop = pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'horaires/stops.txt'))
stop_times = pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'horaires/stop_times.txt'))
transfers = pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'horaires/transfers.txt'))
trips = pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'horaires/trips.txt'))

# liste des gares
LISTE_GARES = (('DUA8775867','Arcueil Cachan',48.79944444,2.32833333),
                ('DUA8727143','Vert-Galant',48.94416667,2.56666667),
                ('DUA8775870','Sceaux',48.78138889,2.29722222),
                ('DUA8775875','Antony',48.75500000,2.30083333),
                ('DUA8775873','Parc de Sceaux',48.77083333,2.31027778),
                ('DUA8775885','Bures Sur Yvette',48.69583333,2.16305556),
                ('DUA8727151','Villeparisis Mitry',48.95305556,2.60277778),
                ('DUA8775862','Port Royal',48.84000000,2.33694444),
                ('DUA8775886','La Hacquiniere',48.69472222,2.15305556),
                ('DUA8775882','Lozere',48.70611111,2.24527778),
                ('DUA8775874','La Croix de Berny',48.76194444,2.30472222),
                ('DUA8775861','Luxembourg',48.84666667,2.34027778),
                ('DUA8727146','Aeroport Ch.De Gaulle 1',49.01000000,2.56055556),
                ('DUA8775877','Les Baconnets',48.73944444,2.28750000),
                ('DUA8775879','Massy Palaiseau',48.72416667,2.25944444),
                ('DUA8775888','Courcelle Sur Yvette',48.70083333,2.09916667),
                ('DUA8727102','Gare du Nord',48.88166667,2.35611111),
                ('DUA8775883','Le Guichet',48.70500000,2.19138889),
                ('DUA8700147','Aeroport Ch.De Gaulle 2',49.00361111,2.57083333),
                ('DUA8775864','Cite Universitaire',48.82055556,2.33888889),
                ('DUA8727152','Mitry-Claye',48.97583333,2.64250000),
                ('DUA8775863','Denfert Rochereau',48.83388889,2.33277778),
                ('DUA8775869','Bourg la Reine',48.78027778,2.31222222),
                ('DUA8775866','Laplace',48.80750000,2.33305556),
                ('DUA8727144','Sevran Beaudottes',48.94805556,2.52444444),
                ('DUA8727147','Blanc-Mesnil',48.93250000,2.47722222),
                ('DUA8778543','Saint Michel',48.85361111,2.34416667),
                ('DUA8727103','Gare du Nord',48.88166667,2.35611111),
                ('DUA8775880','Palaiseau',48.71777778,2.24666667),
                ('DUA8727148','Parc des Expositions',48.97416667,2.51555556),
                ('DUA8775878','Massy Verrieres',48.73444444,2.27361111),
                ('DUA8727130','Aubervilliers',48.92388889,2.38444444),
                ('DUA8775871','Fontenay aux Roses',48.78750000,2.29222222),
                ('DUA8727100','Gare du Nord',48.88166667,2.35611111),
                ('DUA8775872','Robinson',48.78027778,2.28111111),
                ('DUA8727141','Aulnay Sous Bois',48.93222222,2.49583333),
                ('DUA8711300','Gare de l\'Est',48.88166667,2.35611111),
                ('DUA8775889','Saint Remy les Chevreuse',48.70277778,2.07083333),
                ('DUA8775868','Bagneux',48.79333333,2.32138889),
                ('DUA8727145','Villepinte',48.96305556,2.51222222),
                ('DUA8727140','Drancy',48.93277778,2.45472222),
                ('DUA8727142','Sevran-Livry',48.93611111,2.53472222),
                ('DUA8775887','Gif Sur Yvette',48.69833333,2.13666667),
                ('DUA8775881','Palaiseau Villebon',48.70777778,2.23722222),
                ('DUA8727139','Le Bourget',48.93055556,2.42583333),
                ('DUA8775860','Chatelet',48.86138889,2.34638889),
                ('DUA8775876','Fontaine Michalon',48.74333333,2.29638889),
                ('DUA8775865','Gentilly',48.81611111,2.34055556),
                ('DUA8775884','Orsay Ville',48.69750000,2.18194444),
                ('DUA8716479','La Plaine-Stade de France',48.91805556,2.36250000))

# on crée la liste des routes du RER B
liste_des_routes = list(routes[routes['agency_id'] == 'DUA802']['route_id'])

# On s'occupe des voyages ici, avec un set pour exclure des doublons
voyages = pd.DataFrame(columns=["trip_headsign","trip_id"])
gares = []
for route in liste_des_routes:
    liste_des_voyages = trips[trips['route_id']==route]
    for voyage in liste_des_voyages.iterrows():
        liste_arret = [stop_times[stop_times['trip_id']==voyage[1]['trip_id']]]
        for gare in liste_arret[0]['stop_id']:
            gares.append(gare) # ce sont les codes gares qui sont ici

i = 0
for route in liste_des_routes:
    # Uniquement les voyages du RER B
    liste_des_voyages = trips[trips['route_id']==route]
    for voyage in liste_des_voyages.iterrows():
        # Recupere la liste des arrets du voyage
        liste_arret = [stop_times[stop_times['trip_id']==voyage[1]['trip_id']]]
        # Code mission
        code_mission = voyage[1]['trip_headsign']
        # Dates de circulation
        # On garde les noms en anglais pour plus de faciliter dans le code final (absence de traduction)
        jours_circulation = []
        validite_debut = ""
        validite_fin = ""
        if voyage[1]['service_id'] in calendar['service_id'].values:
            if int(calendar[calendar['service_id'] == voyage[1]['service_id']]['monday'].values) == 1:
                jours_circulation.append("Monday")

            if int(calendar[calendar['service_id'] == voyage[1]['service_id']]['tuesday'].values) == 1:
                jours_circulation.append("Tuesday")

            if int(calendar[calendar['service_id'] == voyage[1]['service_id']]['wednesday'].values) == 1:
                jours_circulation.append("Wednesday")

            if int(calendar[calendar['service_id'] == voyage[1]['service_id']]['thursday'].values) == 1:
                jours_circulation.append("Thursday")

            if int(calendar[calendar['service_id'] == voyage[1]['service_id']]['friday'].values) == 1:
                jours_circulation.append("Friday")

            if int(calendar[calendar['service_id'] == voyage[1]['service_id']]['saturday'].values) == 1:
                jours_circulation.append("Saturday")

            if int(calendar[calendar['service_id'] == voyage[1]['service_id']]['sunday'].values) == 1:
                jours_circulation.append("Sunday")
                
            validite_debut = calendar[calendar['service_id'] == voyage[1]['service_id']]['start_date'].values
            validite_fin = calendar[calendar['service_id'] == voyage[1]['service_id']]['end_date'].values
        else:
            pass

        # Arrêts
        for arret in liste_arret[0].iterrows():
            gare = [x[1] for x in LISTE_GARES if x[0] == str(arret[1]['stop_id']).split(':')[1]][0]
            horaire = arret[1]['departure_time']
            for jour in jours_circulation: # zip n'est pas ok ici, ça s'arrêterait beaucoup trop tôt !
                c.execute("INSERT INTO theorie VALUES (?,?,?,?,?,?,?)",[i,code_mission,gare,horaire,jour,validite_debut,validite_fin]) # On n'utilise pas de df parce que sinon, c'est trop long !
                i +=1

# Insert Index in database
c.execute("CREATE INDEX horaire_index ON theorie (Mission, Gare, Horaire, Jour)")