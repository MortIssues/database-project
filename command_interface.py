import sys
import cmd2
from cmd2 import style, Fg, with_argparser
import sys
import argparse
from tabulate import tabulate


class CommandInterface(cmd2.Cmd):
    intro = "CLI for the Lusail Stadium database. Use 'help' or 'help <command>'."
    prompt = "DATABASE> "

    def do_exit(self, args):
        """Exits the program."""
        print("Exiting application.")
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Connection Terminated")
        sys.exit(0)
        return True

    def do_quit(self, args):
        return self.do_exit(args)

    def do_SQL(self, args):
        """Issues an sql command."""
        self.issue_SQL(args)

    show_parser = argparse.ArgumentParser(prog="show")
    subparsers = show_parser.add_subparsers(dest="subcommand")

    database_parser = subparsers.add_parser('database', help="Show contents of a database file.")
    database_parser.add_argument('database_name', type=str, help="Name of the database to show.")
    database_parser.add_argument('-t', '--tabulate', action='store_true', help="Display in tabulated format.")

    location_parser = subparsers.add_parser('location', help="Show location of a specific attendee")
    location_parser.add_argument('attendee_id', type=int, help="ID of the attendee")

    @with_argparser(show_parser)
    def do_show(self, args):
        """Show data from the database based on subcommand. Usage: show <subcommand> [options]"""

        if args.subcommand == "database":
            database_name = args.database_name
            tabulate = args.tabulate

            self.print_database(database_name, tabulate)

        elif args.subcommand == "location":
            attendee_id = args.attendee_id
            self.poutput(f"Showing location for attendee with ID {attendee_id}.")
            self.get_location(attendee_id)

        else:
            self.poutput(style("Error - Unknown subcommand for 'show'", fg=Fg.RED))

    def default(self, statement):
        self.poutput(style(f"Error - Unknown Command: {statement.raw}\n"
                           "Check syntax or use help or help <command>.",
                           fg=Fg.RED))


if __name__ == "__main__":
    interface = CommandInterface()
    interface.cmdloop()
