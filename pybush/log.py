#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a logger
"""

"""
Niveau  Valeur  Usage
CRITICAL    50  Le programme complet est en train de partir en couille.
ERROR   40  Une opération a foirée.
WARNING     30  Pour avertir que quelque chose mérite l’attention : enclenchement d’un mode particulier, detection d’une situation rare, un lib optionelle peut être installée.
INFO    20  Pour informer de la marche du programme. Par exemple : “Starting CSV parsing”
DEBUG   10  Pour dumper des information quand vous débuggez. Par exemple savoir ce qu’il y a dans ce putain de dictionnaire. 
"""

import logging
 
from logging.handlers import RotatingFileHandler
 
# création de l'objet logger qui va nous servir à écrire dans les logs
logger = logging.getLogger()
# on met le niveau du logger à DEBUG, comme ça il écrit tout
logger.setLevel(logging.DEBUG)
 
# création d'un formateur qui va ajouter le temps, le niveau
# de chaque message quand on écrira un message dans le log
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
# création d'un handler qui va rediriger une écriture du log vers
# un fichier en mode 'append', avec 1 backup et une taille max de 1Mo
file_handler = RotatingFileHandler('activity.log', 'a', 1000000, 1)
# on lui met le niveau sur DEBUG, on lui dit qu'il doit utiliser le formateur
# créé précédement et on ajoute ce handler au logger
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
 
# création d'un second handler qui va rediriger chaque écriture de log
# sur la console
steam_handler = logging.StreamHandler()
steam_handler.setLevel(logging.DEBUG)
logger.addHandler(steam_handler)
 
# Après 3 heures, on peut enfin logguer
# Il est temps de spammer votre code avec des logs partout :
logger.info('Hello')
logger.warning('Testing %s', 'foo')
