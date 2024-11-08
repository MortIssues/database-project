class EventManager:
    def create_event_table(self):
        self.cursor.execute(""" 
            CREATE TABLE events (
                ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                title TEXT,
                date TEXT
                ) """)
        self.connection.commit()