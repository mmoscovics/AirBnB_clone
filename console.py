#!/usr/bin/python3
""" Program that contrains the entry point of the command interpreter. """
import cmd
import sys
import json


class HBNBCommand(cmd.Cmd):
    """ Class for the command interpreter. """

    intro = ""
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

    def emptyline(self):
        """Passes on an empty line
        """
        pass

    def do_create(self, arg):
        """Creates a new instance of a class
        Saves it to the JSON file and prints the id
        """

    def do_show(self, arg):
        """Prints the string representation of an instance
        Based on the class name and id
        """

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        Saves the change into the JSON file
        """

    def do_all(self, arg):
        """Prints all string representation of all instances
        Based or not on the class name
        """

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        By adding or updating attribute and saves into JSON file
        """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
