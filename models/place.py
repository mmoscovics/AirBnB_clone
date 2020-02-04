#!/usr/bin/python3
""" Class Place that inherits from BaseModel """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Class Place
    Public Class Attributes:
    city_id: string - empty string: it will be the City.id
    user_id: string - empty string: it will be the User.id
    name: string - empty string
    description: string - empty string
    number_rooms: Integer - 0
    number_bathrooms: Integer - 0
    max_guest: Integer - 0
    price_by_night: Integer - 0
    latitude: float - 0.0
    longitude: float - 0.0
    amenity_ids: list of string - empty list: it will be the list
    of Amenity.id later
    """

    def __init__(self):
        """ Constructor for Public Class Attribute """
        self.city_id = city_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitdue
        self.longitude = longitude
        self.amenity_ids = amenity_ids
