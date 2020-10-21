import random
from flask import Flask, jsonify, request

app = Flask(__name__)

clothes_state = {
    "shoes": "black",
    "jeans": "blue",
    "t-shirt": "white",
    "socks": "red",
    "underwear": "black",
}

@app.route("/clothes")
def clothes():
    return jsonify(list(clothes_state.keys()))

@app.route("/clothes/<name>")
def garment(name):
    color = clothes_state[name]
    return jsonify({"name": name, "color": color})
