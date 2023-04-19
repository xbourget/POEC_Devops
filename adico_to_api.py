#!/usr/bin/python3
# -*- coding: utf-8  -*-

from myLib.scrabble import scrabble
import  json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return json.dumps( scrabble )

@app.route('/lettre')
def lettre():
    dico = { 'lettres' : list(scrabble.keys()) }
    return json.dumps( dico )

@app.route('/toto')
def toto():
    return "bonjour Toto"

@app.route('/avanceTravaux')
def travaux():
    return "términé"

app.run( port=3551)