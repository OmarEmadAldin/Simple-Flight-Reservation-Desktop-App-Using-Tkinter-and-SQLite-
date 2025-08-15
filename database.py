import sqlite3

DB_NAME = "flights.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            flight_number TEXT NOT NULL,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            seat_number TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_reservation(name, flight_number, departure, destination, date, seat_number):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, flight_number, departure, destination, date, seat_number))
    conn.commit()
    conn.close()

def get_reservations():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM reservations")
    rows = cur.fetchall()
    conn.close()
    return rows

def update_reservation(res_id, name, flight_number, departure, destination, date, seat_number):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        UPDATE reservations
        SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
        WHERE id=?
    """, (name, flight_number, departure, destination, date, seat_number, res_id))
    conn.commit()
    conn.close()

def delete_reservation(res_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM reservations WHERE id=?", (res_id,))
    conn.commit()
    conn.close()
