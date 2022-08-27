from flask import Flask

app = Flask(__name__)

@app.route("/calc")
def calc_page():
    return app.route("/calc")

@app.route("/greet")
def greet_page():
   return app.route("/greet")