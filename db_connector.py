from pymongo import MongoClient


# URL = 'mongodb://steno87:110203_Ca@cluster0-shard-00-00-fxpno.mongodb.net:27017,cluster0-shard-00-01-fxpno.mongodb.net:27017,cluster0-shard-00-02-fxpno.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'

ROWS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
COLUMNS = 17


def seats_initialize(rows=ROWS, columns=COLUMNS):
    client = MongoClient("localhost:27017")
    db = client.officina_teatrale_db
    seats = db.seats
    for i in rows:
        for j in range(1, columns):
            print(i + str(j))
            seat = {
                "seat_id": i + str(j),
                "status": "available"
            }
            seats.insert_one(seat)


def seats_reset():
    client = MongoClient("localhost:27017")
    db = client.officina_teatrale_db
    seats = db.seats
    seats.delete_many({})


def get_seats():
    client = MongoClient("localhost:27017")
    db = client.officina_teatrale_db
    seats = db.seats
    return seats.find({})


def update_seat(seat_id, status):
    client = MongoClient("localhost:27017")
    db = client.officina_teatrale_db
    seats = db.seats
    seats.update_one(
        {"seat_id": seat_id},
        {
            "$set": {
                "status": status
            }
        }
    )


def get_seat_status(seat_id):
    client = MongoClient("localhost:27017")
    db = client.officina_teatrale_db
    seats = db.seats
    return seats.find({"seat_id": seat_id})

