# Quali'B

Quali'B fournit et prédit la qualité du trafic du [RER B](https://www.rerb-leblog.fr/) en temps réel.

En se basant sur les horaires théoriques de la SNCF et de la RATP, Quali'B interroge les APIs Temps Réels de ces deux opérateurs de transport et effectue des comparaisons qui lui permettent de définir la qualité du trafic.

[Version live](http://qualib.dreamsinthe.cloud)

## Avant de commencer

Quali'B est basé sur :

* [Open Data SNCF](https://ressources.data.sncf.com/explore/?sort=modified);
* [API Temps Réel Transilien SNCF](https://ressources.data.sncf.com/explore/dataset/api-temps-reel-transilien/);
* [API Temps Réel RATP](https://data.ratp.fr/page/temps-reel/).

Les APIs Temps Réel nécessitent une inscription préalable pour être utilisées !

## Prérequis

Python >=3.5, Node.js >=7.6 et NPM >= 4.3

## Installation

*Installation du serveur web :

    npm install


dans le dossier webserver.

*Installation du backend python :

    virtualenv -p python3  
    source bin/activate  
    pip install -r REQUIREMENTS.TXT

dans le dossier racine.

## Première utilisation

Avant toute utilisation de Quali'B, il est nécessaire de télécharger les horaires théoriques de passage des missions accessible sur [OPEN DATA RATP](https://data.ratp.fr/explore/dataset/offre-transport-de-la-ratp-format-gtfs/) ou [OPEN DATA SNCF](https://ressources.data.sncf.com/explore/dataset/sncf-transilien-gtfs/) au format GTFS.

Après téléchargement, tous les fichiers sont à placer dans le dossier horaires. La génération de la base de données SQLite3 est effectuée via :

    source bin/activate
    python generate_theoretical_timetables.py

Le couple Login/Password pour l'utilisation de l'[API Temps Réel Transilien SNCF](https://ressources.data.sncf.com/explore/dataset/api-temps-reel-transilien/) sont à renseigner dans le fichier _qualib/conf.py_.

Le fichier _Wsiv.wsdl_ à utiliser pour accéder à l'[API Temps Réel RATP](https://data.ratp.fr/page/temps-reel/) est à mettre dans la racine du dossier.

## Tests

    python -m tests.py

## Technos utilisées

### Core
* [Python 3.5](https://www.python.org/)
* [Folium](https://folium.readthedocs.io/en/latest/)
* [Requests](http://docs.python-requests.org/en/master/)
* [Pandas](http://pandas.pydata.org/)
* [Zeep](http://docs.python-zeep.org/en/master/)

* [SQLite3](https://www.sqlite.org/)

### Back-end
* [node.js](https://nodejs.org/en/)
* [npm](https://www.npmjs.com/)
* [express.js](http://expressjs.com/fr/)
* [Babel](https://babeljs.io/)
* [webpack](https://webpack.js.org/)

### Front-end
* [React](https://facebook.github.io/react/)
* [Bootstrap](http://getbootstrap.com/)

## Version

* Alpha (avril 2017) : Affichage du trafic qualitatif en temps réel.

## Auteur
* **Jonathan Perron** - [Mon site](http://www.jonathanperron.fr)

[Liste complète des contributeurs](https://github.com/jonperron/qualib/contributors)

## Licence

Ce projet est distribué sous licence GNU General Public License - voir [LICENSE.md](LICENSE.md) pour plus de détails.

Les horaires et APIs utilisés par Quali'B sont les propriétés de la [SNCF](https://ressources.data.sncf.com/explore/) et de la [RATP](https://data.ratp.fr/explore/?sort=modified) et sont distribués sous [Licence SNCF OPEN DATA](https://ressources.data.sncf.com/explore/) et [Licence RATP OPEN DATA](#) respectivement. Ces matériaux sont accessibles sur les sites de leurs propriétaires respectifs et ne sont pas inclus dans ce projet.

## Remerciements/Acknowledgements

* Tous les membres de la team #RERB Sud pour m'avoir inspiré ce projet.
* [Ardit Sulce](http://arditsulce.com/) for his course *[The Python Mega Course: Build 10 Real World Applications](https://www.udemy.com/the-python-mega-course/)* which helped me a lot in building the core of Quali'B.
* [Kirill Eremenko](https://linkedin.com/in/keremenko) et [Hadelin de Ponteves](https://linkedin.com/in/hadelin-de-ponteves-1425ba5b) for their course *[Machine Learning A-Z™: Hands-On Python & R In Data Science](https://www.udemy.com/machinelearning/)* which allowed me to discover the world of Machine Learning.
