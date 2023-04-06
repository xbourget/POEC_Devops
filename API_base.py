#!/usr/bin/python3
# -*- coding: utf-8  -*-



import flask

from flask import request
import json
import socket
import os
import platform
import psutil


# declaration d'un object serveur
app = flask.Flask(__name__)
nombre_de_roues = {"tram":18, "voiture": 4, "vélo": 2, "tricycle": 3}

mem=psutil.virtual_memory()

print(__file__)

#app.config["DEBUG"] = True
@app.route('/', methods=['GET'])
def toto():
 release = platform.release
 print (mem, type)
 dico = {"hostname" : socket.gethostname(),
         "AddresseIpDylan" :socket.gethostbyname(socket.gethostname),
         "version": platform.release,
         "memFreeV"  :mem.free / (1000*1000*1000),
         "memTotalI"  :"{0:5.2f} Go".format(mem.total /(1024*1024*1024)),
         "memFreeI" : mem.free >> 30
                                         }
 return dico

#Requete et ne pas oublier le décorateur
#Decorateur/ encapsuler la fonction / post traitement
@app.route('/aurevoir', methods=['GET'])
def bye():
 return "Bye bye"

#Requete et ne pas oublier le décorateur
#Decorateur/ encapsuler la fonction / post traitement
@app.route('/vehicule', methods=['GET'])
def vehicule():
 nom =request.args.get('nom')
 return json.dumps(nombre_de_roues[ nom ])


app.run()