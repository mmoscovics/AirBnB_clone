#!/usr/bin/python3
""" Class FileStorage that serializes instances to a JSON file and deserializes
JSON file to instances. """
import json
import os


class FileStorage:
    """ Class that serializes and deserializes JSON file. """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary. """

        return type(self).__objects

    def new(self, obj):
        """ Sets object with key. """

        type(self).__objects[type(obj).__name__ + '.' + obj.id] = obj

    def save(self):
        """ Serializes to JSON file. """

        dict_obj = {key: value.to_dict() for key, value in
                    type(self).__objects.items()}
        with open(type(self).__file_path, "w+") as j_file:
            json.dump(dict_obj, j_file)

    def reload(self):
        """ Deserializes the JSON file to objects. """

        if os.path.exists(type(self).__file_path):
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review
            class_names = {"BaseModel": BaseModel,
                           "User": User}

            with open(type(self).__file_path, 'r') as j_file:
                dict_obj = json.load(j_file)
                for k, v in dict_obj.items():
                    FileStorage.__objects[k] = class_names[v["__class__"]](**v)
