from flask import Flask, jsonify, render_template
import random
import datetime

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

@app.route("/api/whataweek")
def api_whataweek():
    weekday = datetime.datetime.today().weekday()
    if weekday <= 4:
        return jsonify({"img": f"https://images.nanoy.fr/whataweek/{weekday}.jpg", "msg": "ok"})
    return jsonify({"img": "", "msg": "weekend"})


if __name__ == "__main__":
    app.run()
