import random
from flask import Flask, jsonify, request, abort, url_for, Response

app = Flask(__name__)

def get_about_me_data():
    return {
    "name": "Mia",
    "surname": "Bajic",
    "eyes_count": 2,
    "eyes color": "brown",
    "hands count": 2,
    "legs count": 2,
    "hair color": "blond",
    "mood": random.choice(["cheerful", "grumpy", "comfortably numb"]),
}

@app.route("/")
def about_me():
    return jsonify(get_about_me_data())

def get_movies(name=None):
    movies = [
        {"name": "The Last Boy Scout", "year": 1991},
        {"name": "Mies vailla menneisyyttä", "year": 2002},
        {"name": "Sharknado", "year": 2013},
        {"name": "Mega Shark vs. Giant Octopus", "year": 2009},
    ]
    if name is not None:
        filtered_movies = []
        for movie in movies:
            if name in movie["name"].lower():
                filtered_movies.append(movie)
        return filtered_movies
    else:
        return movies

@app.route("/movies")
def movies():
    return jsonify(get_movies(name=request.args.get("name")))


clothes_state = {
    "shoes": "brown",
    "jeans": "blue",
    "t-shirt": "white",
    "socks": "red",
    "underwear": "black",
}

@app.route("/clothes", methods=["GET", "POST"])
def clothes():
    if request.method == "POST":
        new_garment = request.get_json()
        name, color = new_garment["name"], new_garment["color"]

        clothes_state[name] = color

        response = jsonify(list(clothes_state.keys()))
        response.status_code = 201
        response.headers["Location"] = url_for('garment', name=name)
        return response
    else:
        return jsonify(list(clothes_state.keys()))

@app.route("/clothes/<name>", methods=["GET", "DELETE"])
def garment(name):
    try:
        if request.method == "DELETE":
            if name == 'underwear':
                return Response(status=403)  # nic takového!
            else:
                del clothes_state[name]
                return Response(status=204)
        else:
            color = clothes_state[name]
            return jsonify({"name": name, "color": color})
    except KeyError:
        abort(404)
