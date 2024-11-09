import sqlite3
from attendee_manager import AttendeeManager
from event_manager import EventManager
from command_interface import CommandInterface

class DatabaseManager(AttendeeManager, EventManager, CommandInterface):
    def __init__(self):
        super().__init__()
        try:
            self.connection = sqlite3.connect("lusail_stadium.db")
            self.cursor = self.connection.cursor()
            print("Database Initialised")

            self.cursor.execute("select sqlite_version();")
            print("SQLite Version is {}".format(self.cursor.fetchall()))
        except sqlite3.Error as error:
            print("Error Occurred - \n", error)

    def __del__(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Connection Terminated")

    def get_column_names(self, table):
        self.cursor.execute("PRAGMA table_info(?)", (table,))

    def exit_program(self, args):
        print("Exiting application.")
        self.connection.close()
        return "exit"