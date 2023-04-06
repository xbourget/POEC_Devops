#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ] { }


import json
import psutil
from flask import Flask

app = Flask(__name__)

classe = { 
              'john'  : { 'nat' : 'eng', "sport" : 'course' },
              'dylan' : { 'nat' : 'bzh', 'music': [ 'jazz', 'blues'], 'cuisine' : 'japonais'  },
              'marius' : { 'pointure' : 45, 'cuisine' : [ 'poisson gri', 'ratatouille']  }
        }
 

@app.route('/')
def index():
    return json.dumps( classe )


@app.route('/mem')
def mem():
    dico = { "mem" : psutil.cpu_percent(4) }
    return json.dumps( dico )

app.run()