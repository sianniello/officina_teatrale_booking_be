from pymongo import MongoClient


ROWS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']
COLUMNS = [[6, 10, 6],
           [10, 14, 9],
           [11, 14, 11],
           [11, 15, 11],
           [11, 14, 11],
           [13, 15, 13],
           [13, 14, 13],
           [15, 14, 15],
           [15, 15, 15],
           [15, 14, 15],
           [16, 15, 16],
           [15, 14, 15],
           [15, 15, 15],
           [13, 14, 13],
           [13, 15, 13],
           [12, 14, 12],
           [12, 15, 12],
           [11, 15, 11],
           [11, 14, 11],
           [11, 15, 11],
           [11, 14, 11],
           [11, 15, 11],
           [12, 14, 12],
           [12, 14, 11],
           [12, 13, 12]
           ]
# URL = "localhost:27017"
URL = "mongodb://steno87:110203_Ca@cluster0-shard-00-00-fxpno.mongodb.net:27017,cluster0-shard-00-01-fxpno.mongodb.net:27017,cluster0-shard-00-02-fxpno.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin"
DATABASE = "officina_teatrale_db"

client = MongoClient(URL)
db = client[DATABASE]
seats = db.seats
bookings = db.bookings


def seats_initialize(rows=ROWS, columns=COLUMNS):
    for idx, i in enumerate(rows):
        for j in range(0, columns[idx][0]):
            seat = {
                "seat_id": i + "S" + str(j + 1),
                "status": "available"
            }
            seats.insert_one(seat)
        for j in range(0, columns[idx][1]):
            seat = {
                "seat_id": i + "C" + str(j + 1),
                "status": "available"
            }
            seats.insert_one(seat)
        for j in range(0, columns[idx][2]):
            seat = {
                "seat_id": i + "D" + str(j + 1),
                "status": "available"
            }
            seats.insert_one(seat)


def seats_reset():
    seats.delete_many({})


def get_seats():
    return seats.find({})


def book_seat(booking):
    if check_seats_available(booking['seats']):
        for seat in booking['seats']:
            seats.update_one(
                {"seat_id": seat['id'].replace("_", "")},
                {
                    "$set": {
                        "status": seat['type']
                    }
                }
            )
        bookings.insert_one(booking)
        return True
    else:
        return False


def check_seats_available(seats_to_check):
    for seat in seats_to_check:
        seat = seats.find_one({"seat_id": seat['id'].replace("_", "")})
        if seat is None or seat['status'] != "available":
            return False
    return True


def get_seat_status(seat_id):
    return seats.find_one({"seat_id": seat_id.replace("_", "")}).status


def bookings_reset():
    bookings.delete_many({})


seats_reset()
bookings_reset()
seats_initialize()
