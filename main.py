from database_manager import DatabaseManager

def main():
    db = DatabaseManager()
    db.cmdloop()

    del db

if __name__ == '__main__':
    main()