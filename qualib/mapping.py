# /usr/bin/python3
# -*- coding : utf-8 -*-

"""
Quali'B map functions used to tune icon colors.
"""

__author__ = "Jonathan Perron"
__version__ = "1.0"
__maintainer__ = "Jonathan Perron"
__email__ = "contact@jonathanperron.fr"
__repo__ = "https://github.com/jonperron/qualib"

def color(trafic):
    if trafic == "Normal":
        return "green"
    elif trafic == "Retard leger":
        return "orange"
    elif trafic == "Retard important":
        return "red"
    elif trafic == "Supprime":
        return "black"
    else:
        return "white"

def icon(trafic):
    if trafic == "Normal":
        return "check"
    elif trafic == "Retard leger":
        return "info-sign"
    elif trafic == "Retard important":
        return "info-sign"
    elif trafic == "Supprime":
        return "exclamation-sign"
    else:
        return "question-sign"    

def icon_color(trafic):
    if trafic == "Normal":
        return "white"
    elif trafic == "Retard leger":
        return "white"
    elif trafic == "Retard important":
        return "white"
    elif trafic == "Supprime":
        return "white"
    else:
        return "black" 