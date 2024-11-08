import sqlite3
import webbrowser
from time import strftime, gmtime


class AttendeeManager:
    def create_attendee_table(self):
        self.cursor.execute(""" 
            CREATE TABLE attendees (
                ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                forename TEXT,
                surname TEXT,
                email TEXT,
                registered_event_ID INTEGER,
                zone INTEGER,
                seat INTEGER,
                vehicle_registration TEXT,
                latitude FLOAT,
                longitude FLOAT,
                update_time TEXT
                ) """)
        self.connection.commit()

    def add_attendee(self, f_name, s_name, email, event_id, zone, seat, vehicle_reg):
        self.cursor.execute(""" 
            INSERT INTO attendees (
                forename,
                surname,
                email,
                registered_event_ID,
                zone,
                seat,
                vehicle_registration) 
            VALUES (?, ?, ?, ?, ?, ?, ?) """,
                (f_name, s_name, email, event_id, zone, seat, vehicle_reg))
        self.connection.commit()

    def set_location(self, id, lat, lon):
        self.cursor.execute("""
            UPDATE attendees
            SET latitude = ?, longitude = ?, update_time = ?
            WHERE ID = ?""",
            (lat, lon, strftime("%H %M %S", gmtime()), id))
        self.connection.commit()

    def get_location(self, id):
        self.cursor.execute("""
            SELECT latitude 
            FROM attendees 
            WHERE ID = ?""",
            (id,))
        lat = (str(self.cursor.fetchall())
               .replace("[(", '')
               .replace(")]", ''))
        self.cursor.execute("""
            SELECT longitude 
            FROM attendees
            WHERE ID = ?""",
            (id,))
        lon = (str(self.cursor.fetchall())
               .replace("[(", '')
               .replace(")]", ''))
        webbrowser.open("https://www.google.co.uk/maps/search/"
                        + lat + lon + "/@" + lat + lon + "100m/")

