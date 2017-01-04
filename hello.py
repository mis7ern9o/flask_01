# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 00:12:21 2017

@author: misterneo
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')

def index():
    return 'Hello world!'
    
if __name__ == '__main__':
    app.run(debug=True)