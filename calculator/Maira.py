# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 20:32:23 2021

@author: maira
"""
import os  # sistema operacional
import math
import numpy as np
from flask import Flask, request #framework, biblioteca
app = Flask(__name__)

@app.route("/api/calc", methods=["GET"])
def calculator():
    # expressoes matematicas contendo o simbolo '+' funcionam seguidas de %2B
    exp = request.args.get("exp", type=str)
    
    return {'result': eval(exp)}
   

host = os.getenv('IP', '0.0.0.0') # valor chave ou valor padrao
port = int(os.getenv('PORT', 8000))

app.run(host=host, port=port)