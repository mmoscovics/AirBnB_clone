#!/usr/bin/python3
""" Program that contrains the entry point of the command interpreter. """
import cmd
import sys
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class_names = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}


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

    def do_create(self, name):
        """Creates a new instance of a class
        Saves it to the JSON file and prints the id
        """

        if not name:
            print("** class name missing **")
            return
        elif name not in class_names:
            print("** class doesn't exist **")
            return
        else:
            inst = class_names[name]()
            storage.save()
            print(inst.id)

    def do_show(self, name):
        """Prints the string representation of an instance
        Based on the class name and id
        """

        if not name:
            print("** class name missing **")
            return
        args = name.split()
        if not args[0] in class_names:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            obj = args[0] + '.' + args[1]
            if obj not in storage.all():
                print("** no instance found **")
                return
            print(storage.all()[obj])

    def do_destroy(self, name):
        """Deletes an instance based on the class name and id
        Saves the change into the JSON file
        """

        if not name:
            print("** class name missing **")
            return
        args = name.split()
        if not args[0] in class_names:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            obj = args[0] + '.' + args[1]
            if obj not in storage.all():
                print("** no instance found **")
                return
            del storage.all()[obj]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        Based or not on the class name
        """

        if arg:
            args = arg.split()
            if not args[0] in class_names:
                print("** class doesn't exist **")
                return
            else:
                obj = args[0]
                print(storage.all()[obj])
                return
        else:
            print(storage.all())

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        By adding or updating attribute and saves into JSON file
        """

        stor_all = storage.all()
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if not args[0] in class_names:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        else:
            temp = args[3]
            if temp[0] is '"' and temp[-1] is '"':
                temp = temp[1:-1]
            obj = args[0] + "." + args[1]
            stor_all[obj].__dict__.update({args[2]: temp})
            storage.save()
            return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
