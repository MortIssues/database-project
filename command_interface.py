import sys
import cmd2
from cmd2 import style, Fg
import sys
from tabulate import tabulate


class CommandInterface(cmd2.Cmd):
    intro = "CLI for the Lusail Stadium database. Use 'help' or 'help <command>'."
    prompt = "DATABASE> "

    def __init__(self):
        super().__init__()

    def do_exit(self, args):
        """Exits the program."""
        print("Exiting application.")
        sys.exit(0)
        return True

    def do_quit(self, args):
        return self.do_exit(args)

    def default(self, statement):
        self.poutput(style(f"Error - Unknown Command: {statement.raw}\n"
                           f"Check syntax or use help or help <command>.",
                           fg=Fg.RED))


if __name__ == "__main__":
    interface = CommandInterface()
    interface.cmdloop()
