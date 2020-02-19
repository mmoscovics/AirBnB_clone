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

    def default(self, arg):
        """Breaks down argument to be passed to other commands
        """

        if '.' not in arg:
            return(cmd.Cmd.default(self, arg))
        print(arg)
        command_class = arg.split('.')
        print(command_class)
        _class = command_class[0]
        trans = {40: 32, 41: None, 34: None, 44: None}
        commands = (command_class[1].translate(trans)).split(' ')
        command = commands[0]
        print(commands)
        if command == "show":
            _id = commands[1]
            self.do_show(_class + ' ' + _id)
        elif command == "destroy":
            _id = commands[1]
            self.do_destroy(_class + ' ' + _id)
        elif command == "all":
            self.do_all(_class)
        elif command == "update":
            if len(commands) < 2:
                print("** instance id missing **")
                return
            elif len(commands) < 3:
                print("** attribute name missing **")
                return
            elif len(commands) < 4:
                print("** value missing **")
                return
            _id = commands[1]
            key = commands[2]
            val = commands[3]
            self.do_update(_class + ' ' + _id + ' ' + key + ' ' + val)

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
            if not arg in class_names:
                print("** class doesn't exist **")
                return
            else:
                for key in storage.all():
                    if arg == key.split('.')[0]:
                        print(storage.all()[key])
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
