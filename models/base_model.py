#!/usr/bin/python3
""" Class BaseModel that defines all common attributes/methods
for other classes.
"""
from datetime import datetime as dt
from uuid import uuid4 as uid
from models import storage


class BaseModel:
    """Class BaseModel
    Public Instance Attributes:
    Id - string assigned with an uuid
    Created-at - datetime assigned with current datetime when created
    Updated-at - datetime assigned with current datetime when updated
    """

    def __init__(self, *args, **kwargs):
        """Constructor for Public Instance Attributes """

        if kwargs and kwargs is not []:
            self.id = kwargs["id"]
            self.created_at = dt.strptime(kwargs["created_at"],
                                          "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = dt.strptime(kwargs["updated_at"],
                                          "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uid())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            storage.new(self)

    def __str__(self):
        """Prints class name, id, and dict"""

        return ("[{}] ({}) {}".format(type(self).__name__,
                self.id, self.__dict__))

    def save(self):
        """Updates the public instance attribute 'updated_at with dt'"""

        self.updated_at = dt.now()
        storage.save()

    def to_dict(self):
        """Returns a dict containing all keys/values of __dict__"""

        new_dict = dict(self.__dict__)
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
