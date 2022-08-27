from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def say_hello():
    return "welcome"

@app.route("/welcome/home")
def say_hello2():
    return "welcome home"
    
@app.route("/welcome/back")
def say_hello3():
    return "weclome back"