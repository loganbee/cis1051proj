from flask import Flask, redirect, render_template, request

import random

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/thoughts")
def thoughts():
    name = request.args.get("name")
    return render_template("thoughts.html", name=name)
