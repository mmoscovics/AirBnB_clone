#!/usr/bin/python3
""" Class FileStorage that serializes instances to a JSON file and deserializes
JSON file to instances. """
import json
import sys


class FileStorage:
    """ Class that serializes and deserializes JSON file. """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Returns the dictionary. """

        return type(self).__objects

    def new(self, obj):
        """ Sets object with key. """


    def save(self):
        """ Serializes to JSON file. """


    def reload(self):
        """ Deserializes the JSON file to objects. """
