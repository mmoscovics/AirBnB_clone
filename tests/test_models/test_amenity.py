#!/usr/bin/python3
""" Tests for class Amenity """

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from tests.test_models.test_base_model import TestBaseModel


class TestAmenity(TestBaseModel):
    """ Amenity Tests """

    def __init__(self, *args, **kwargs):
        """ Constructor attributes and objects to test """

        super().__init__(*args, **kwargs)
        self._class = Amenity
        self._name = "Amenity"
