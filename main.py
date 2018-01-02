from utils import *
from flask import Flask, request, jsonify
from flask_cors import CORS
import db_connector as dbc

app = Flask(__name__, template_folder="static")
CORS(app)


@app.route("/bookings", methods=['GET'])
def bookings():
    seats = dbc.get_seats()
    resp = seat_map_encoding(seats)
    print(resp)
    resp_json = jsonify(
        seat_map=resp,
        rows=['A', 'B', 'C', ' ', 'D', 'E', 'F', 'G'],
        columns=['1', '2', '3', '4', ' ',
                 '5', '6', '7', '8', '9', '10', '11', '12', ' ',
                 '13', '14', '15', '16']
    )
    return resp_json


@app.route("/bookings", methods=['POST'])
def new_booking():
    booking_json = request.get_json()
    print(booking_json)
    if dbc.book_seat(booking_json):
        return jsonify(seats=booking_json['seats']), 201
