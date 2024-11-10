import sqlite3
from tabulate import tabulate
from cmd2 import style, Fg, with_argparser
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

    def issue_sql(self, cmd):
        self.cursor.execute(cmd)
        self.connection.commit()

    def print_database(self, table_name, is_tabulated):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        rows = self.cursor.fetchall()
        column_names = [description[0] for description in self.cursor.description]

        if is_tabulated:
            print(tabulate(rows, headers=column_names, tablefmt="simple_outline"))
        else:
            for row in rows:
                print(row)