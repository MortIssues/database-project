import tabulate

class CommandInterface:
    def __init__(self):
        self.commands = {
            "exit": self.exit_program,
            "show_database": self.show_database,
            "show_details": self.show_attendee_details,
            "add": self.add_attendee,
            "remove": self.remove_attendee
        }

    def show_database(self, args):
        if not args:
            print("Usage: show <table_name> [-t/--tabulate]")
            return

        file = args[0]
        is_tabulated = "-t" in args or "--tabulate" in args
        self.cursor.execute("SELECT * FROM attendees")
        if is_tabulated:
            print(tabulate(self.cursor.fetchall(), tablefmt="simple_grid"))
        else:
            print(self.cursor.fetchall())

    def parse_command(self, command_str):
        parts = command_str.strip().split()
        if not parts:
            return
        command = parts[0]
        args = parts[1:]
        print(command, "\n", args)

        if command == "show" and len(args) > 0 and args[0] == "details":
            command_key = "show_details"
            args = args[1:]
        else:
            command_key = command

        if command_key in self.commands:
            result = self.commands[command_key](args)
            if result == "exit":
                return "exit"
        else:
            print(f"Error Occurred - Unknown command: '{command_str}'")