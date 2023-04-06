#!/usr/bin/python3
# -*- coding: utf-8  -*-

import flask
import json
import socket
import os
import platform
import psutil

# declaration d'un objet server
app = flask.Flask(__name__)

print( type(app) )

@app.route('/', methods=['GET'])
def name():
    return "<h1>bonjour</h1>"

@app.route('/getinfo', methods=['GET'])
def info():
    #release = os.system("uname")
    release = platform.release()

    mem = psutil.virtual_memory() 
    print( mem, type(mem) )
    dico = {    "name"      : socket.gethostname(), 
                "IP"        : socket.gethostbyname(socket.gethostname()),
                "version"   : platform.release(),
                "memFree"       : "{0:5.2f} Go".format( mem.free /  (1024 * 1024 * 1024 ) )
            }
    
    return json.dumps( dico )


app.run()

