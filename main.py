from utils import *
from flask import Flask, request, render_template
import db_connector as dbc

app = Flask(__name__, template_folder="static")


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/bookings", methods=['GET'])
def bookings():
    seats = dbc.get_seats()
    resp = seat_map_encoding(seats)
    return resp


@app.route("/bookings", methods=['POST'])
def new_booking():
    booking_json = request.get_json()
    print(booking_json)
    return "OK"
