from pymongo import MongoClient



ROWS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
COLUMNS = 17
URL = "localhost:27017"
# URL = "mongodb://steno87:110203_Ca@cluster0-shard-00-00-fxpno.mongodb.net:27017,cluster0-shard-00-01-fxpno.mongodb.net:27017,cluster0-shard-00-02-fxpno.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin"
DATABASE = "officina_teatrale_db"

def seats_initialize(rows=ROWS, columns=COLUMNS):
    client = MongoClient(URL)
    db = client.DATABASE
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
    client = MongoClient(URL)
    db = client.DATABASE
    seats = db.seats
    seats.delete_many({})


def get_seats():
    client = MongoClient(URL)
    db = client.DATABASE
    seats = db.seats
    return seats.find({})


def update_seat(seat_id, status):
    client = MongoClient(URL)
    db = client.DATABASE
    seats = db.seats
    seats.update_one(
        {"seat_id": seat_id},
        {
            "$set": {
                "status": status
            }
        }
    )


def check_seat_available(seat_id, seats):
    seat = seats.find({"seat_id": seat_id})
    if seat.status == "available":
        return True
    else:
        return False


def get_seat_status(seat_id):
    client = MongoClient(URL)
    db = client.DATABASE
    seats = db.seats
    return seats.find({"seat_id": seat_id})


seats_initialize()