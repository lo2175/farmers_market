# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("Farmer's Market Finder...")
    #return "Welcome Home"
    return render_template("home.html")

@home_routes.route("/seasonality")
def about():
    print("Seasonality...")
    return render_template("seasonality.html")
