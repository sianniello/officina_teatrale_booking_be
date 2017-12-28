from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/bookings", methods='GET')
def bookings():
    return


@app.route("/bookings", methods=['POST'])
def new_booking():
    booking_json = request.get_json()
    print(booking_json)
    return "OK"
