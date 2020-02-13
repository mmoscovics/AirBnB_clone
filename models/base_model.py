#!/usr/bin/python3
""" Class BaseModel that defines all common attributes/methods
for other classes. """
import datetime from datetime as dt
import uuid.4 from uuid as uid


class BaseModel:
    """ Class BaseModel
    Public Instance Attributes:
    Id - string assigned with an uuid
    Created-at - datetime assigned with current datetime when created
    Updated-at - datetime assigned with current datetime when updated
    """

    def __init__(self):
        """ Constructor for Public Instance Attributes """

        self.id = uid
        self.created_at = dt
        self.updated_at = dt

    
