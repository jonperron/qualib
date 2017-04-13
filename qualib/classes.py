# /usr/bin/python3
# -*- coding : utf-8 -*-

"""
Quali'B classes.
"""

from datetime import datetime

class Mission:
    """
    Contain a RT Mission
    """
    def __init__(self,station="",code="",date="",network="",stops=False):
        self.station = station
        self.code = code
        self.date = date
        self.network = network
        self.stops = stops

    def create_mission(self,station,code,network,stops):
        self.station = station
        self.code = code
        self.network = network
        self.stops = stops

    def get_mission_date(self,mission):
        if self.network == "SNCF":
            self.date = datetime.strptime(mission.find("date").text,"%d/%m/%Y %H:%M")
        else:
            try:
                self.date = datetime.strptime(mission['stationsDates'][0],'%Y%m%d%H%M') 
            except IndexError: #sometimes, is empty
                self.date = ""

class Gares:
    # liste des gares
    # GTFS, Nom, Longitude, Latitude, ID SNCF
    LISTE_GARES = (('DUA8775867','Arcueil Cachan',48.79944444,2.32833333,None),
                    ('DUA8727143','Vert-Galant',48.94416667,2.56666667,'87271437'),
                    ('DUA8775870','Sceaux',48.78138889,2.29722222,None),
                    ('DUA8775875','Antony',48.75500000,2.30083333,None),
                    ('DUA8775873','Parc de Sceaux',48.77083333,2.31027778,None),
                    ('DUA8775885','Bures Sur Yvette',48.69583333,2.16305556,None),
                    ('DUA8727151','Villeparisis Mitry',48.95305556,2.60277778,'87271510'),
                    ('DUA8775862','Port Royal',48.84000000,2.33694444,None),
                    ('DUA8775886','La Hacquiniere',48.69472222,2.15305556,None),
                    ('DUA8775882','Lozere',48.70611,2.211667,None),
                    ('DUA8775874','La Croix de Berny',48.76194444,2.30472222,None),
                    ('DUA8775861','Luxembourg',48.84666667,2.34027778,None),
                    ('DUA8727146','Aeroport Ch.De Gaulle 1',49.01000000,2.56055556,'87271460'),
                    ('DUA8775877','Les Baconnets',48.73944444,2.28750000,None),
                    ('DUA8775879','Massy Palaiseau',48.72416667,2.25944444,None),
                    ('DUA8775888','Courcelle Sur Yvette',48.70083333,2.09916667,None),
                    ('DUA8727102','Gare du Nord',48.88166667,2.35611111,'87271007'),
                    ('DUA8775883','Le Guichet',48.70500000,2.19138889,None),
                    ('DUA8700147','Aeroport Ch.De Gaulle 2',49.00361111,2.57083333,'87001479'),
                    ('DUA8775864','Cite Universitaire',48.82055556,2.33888889,None),
                    ('DUA8727152','Mitry-Claye',48.97583333,2.64250000,'87271528'),
                    ('DUA8775863','Denfert Rochereau',48.83388889,2.33277778,None),
                    ('DUA8775869','Bourg la Reine',48.78027778,2.31222222,None),
                    ('DUA8775866','Laplace',48.80750000,2.33305556,None),
                    ('DUA8727144','Sevran Beaudottes',48.94805556,2.52444444,'87271445'),
                    ('DUA8727147','Blanc-Mesnil',48.93250000,2.47722222,'87271478'),
                    ('DUA8778543','Saint Michel',48.85361111,2.34416667,None),
                    ('DUA8727103','Gare du Nord',48.88166667,2.35611111,'87271031'),
                    ('DUA8775880','Palaiseau',48.71777778,2.24666667,None),
                    ('DUA8727148','Parc des Expositions',48.97416667,2.51555556,'87271486'),
                    ('DUA8775878','Massy Verrieres',48.73444444,2.27361111,None),
                    ('DUA8727130','Aubervilliers',48.92388889,2.38444444,'87271304'),
                    ('DUA8775871','Fontenay aux Roses',48.78750000,2.29222222,None),
                    ('DUA8727100','Gare du Nord',48.88166667,2.35611111,'87271023'),
                    ('DUA8775872','Robinson',48.78027778,2.28111111,None),
                    ('DUA8727141','Aulnay Sous Bois',48.93222222,2.49583333,'87271411'),
                    # ('DUA8711300',"Gare de l\'Est",48.88166667,2.35611111,'87113001'),
                    ('DUA8775889','Saint Remy les Chevreuse',48.70277778,2.07083333,None),
                    ('DUA8775868','Bagneux',48.79333333,2.32138889,None),
                    ('DUA8727145','Villepinte',48.96305556,2.51222222,'87271452'),
                    ('DUA8727140','Drancy',48.93277778,2.45472222,'87271403'),
                    ('DUA8727142','Sevran-Livry',48.93611111,2.53472222,'87271429'),
                    ('DUA8775887','Gif Sur Yvette',48.69833333,2.13666667,None),
                    ('DUA8775881','Palaiseau Villebon',48.70777778,2.23722222,None),
                    ('DUA8727139','Le Bourget',48.93055556,2.42583333,'87271395'),
                    ('DUA8775860','Chatelet',48.86138889,2.34638889,None),
                    ('DUA8775876','Fontaine Michalon',48.74333333,2.29638889,None),
                    ('DUA8775865','Gentilly',48.81611111,2.34055556,None),
                    ('DUA8775884','Orsay Ville',48.69750000,2.18194444,None),
                    ('DUA8716479','La Plaine-Stade de France',48.91805556,2.36250000,'87164798'))