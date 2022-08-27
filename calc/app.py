# Put your app in here.
from flask import Flask, request

import operations

app = Flask(__name__)

from operations import add, sub, mult, div

@app.route("/add")
def add_route():
    a = request.args["a"]
    b = request.args["b"]

    result = add(int(a),int(b))
    return str(result)

@app.route("/sub")
def sub_route():
    a = request.args["a"]
    b = request.args["b"]

    result = sub(int(a),int(b))
    return str(result)

@app.route("/mult")
def mult_route():
    a = request.args["a"]
    b = request.args["b"]

    result = mult(int(a),int(b))
    return str(result)

@app.route("/div")
def div_route():
    a = request.args["a"]
    b = request.args["b"]

    result = div(int(a),int(b))
    return str(result)