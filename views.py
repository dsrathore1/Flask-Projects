# from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask import *

views = Blueprint(__name__, 'views')


@views.route("/")
def home():
    return "Hello Brother, Welcome to the home"


@views.route("/home")
def name_query():
    return render_template("index.html", name="King", age=21)


@views.route("/home/<username>")
def home2(username):
    return render_template("index.html", name=username)


@views.route("/query")
def query():
    args = request.args
    name = args.get("name")
    return render_template("index.html", name=name)


@views.route("/json")
def get_json():
    return jsonify({"name": "Savan",
                    "age": 32,
                    "love_prolang": True,
                    "father_name": "Sanjay Rathore",
                    "mother_name": "Rajeshree Rathore"
                    })


@views.route("/back")
def go_to_home():
    return redirect(url_for("views.home"))
