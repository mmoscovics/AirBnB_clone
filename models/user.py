#!/usr/bin/python3
""" Class User that inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """Class User
    Public Instance Attributes:
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """

    def __init__(self):
        """ Constructor for Public Instance Attributes """

        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
