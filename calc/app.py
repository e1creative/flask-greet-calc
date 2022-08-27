# Put your app in here.
from flask import Flask, request

from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/<func>")
def route(func):
    print(request.args)

    a = int(request.args["a"])
    b = int(request.args["b"])

    functions = {
        "add": add(a,b),
        "sub": sub(a,b),
        "mult": mult(a,b),
        "div": div(a,b)
    }

    result = functions[func]

    return f"RESULT: {result}"