#!/usr/bin/python3
""" Program that contrains the entry point of the command interpreter. """
import cmd, sys


class HBNBCommand(cmd.Cmd):
    """ Class for the command interpreter. """

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Reads EOF and exits
        """
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
