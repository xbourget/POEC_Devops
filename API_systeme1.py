#!/usr/bin/python3
# -*- coding: utf-8  -*-

import flask
from flask import request
import json
import socket


# declaration d'un objet server
app = flask.Flask(__name__)

nombre_de_roues = {"tram":18, "voiture": 4, "vélo": 2, "tricycle": 3}

#app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def name():
 dico = { "hostname" : socket.gethostname(),
          }
 return json.dumps( dico )

@app.route('/vehicule', methods=['GET'])
def vehicule():
    nom = request.args.get('nom')
    return json.dumps( nombre_de_roues[ nom ] )

app.run()