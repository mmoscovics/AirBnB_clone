#!/usr/bin/python3
""" Class Review that inherits from BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Review
    Public Class Attribute:
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """

    def __init__(self):
        """ Constructor for Public Class Attributes """
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
