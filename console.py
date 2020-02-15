#!/usr/bin/python3
""" Program that contrains the entry point of the command interpreter. """
import cmd
import sys
import json
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Class for the command interpreter. """

    intro = ""
    prompt = "(hbnb) "
    class_names = {"BaseModel": BaseModel}

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

    def do_create(self, name):
        """Creates a new instance of a class
        Saves it to the JSON file and prints the id
        """

        if not name:
            print("** class name missing **")
        elif name not in type(self).class_names:
            print("** class doesn't exist **")
        else:
            inst = BaseModel()
            storage.save()
            print(inst.id)

    def do_show(self, name, class_id):
        """Prints the string representation of an instance
        Based on the class name and id
        """

        if not name and not class_id:
            print("** class name missing **")
        elif name not in type(self).class_names:
            print("** class doesn't exist **")
        elif not class_id:
            print("** instance id missing **")
        elif class_id is not inst.id:
            print("** no instance found **")
        else:
            print(inst)

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
