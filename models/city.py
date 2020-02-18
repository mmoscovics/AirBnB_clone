#!/usr/bin/python3
""" Class City that inherits from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ Class City
    Public Class Attribute:
    state_id: string - empty string: it will be the State.id
    name: string - empty string
    """

    state_id = ""
    name = ""
