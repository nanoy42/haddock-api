from flask import Flask, jsonify, render_template
import random

from haddock import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/vocabulaire")
def vocabulary():
    return jsonify({"msg": random.choice(VOCABULARY)})


@app.route("/api/insultes")
def insult():
    return jsonify({"msg": random.choice(INSULTS)})


if __name__ == "__main__":
    app.run()
