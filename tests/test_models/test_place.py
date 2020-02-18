#!/usr/bin/python3
""" Tests for class Place """

import unittest
from models.base_model import BaseModel
from models.place import Place
from tests.test_models.test_base_model import TestBaseModel


class TestPlace(TestBaseModel):
    """ Place Tests """

    def __init__(self, *args, **kwargs):
        """ Constructor attributes and objects to test """

        super().__init__(*args, **kwargs)
        self._class = Place
        self._name = "Place"

    def test__class_attrs(self):
        """ Test for attributes """

        self.assertIsInstance(self._class.city_id, str)
        self.assertIsInstance(self._class.user_id, str)
        self.assertIsInstance(self._class.name, str)
        self.assertIsInstance(self._class.description, str)
        self.assertIsInstance(self._class.number_rooms, int)
        self.assertIsInstance(self._class.number_bathrooms, int)
        self.assertIsInstance(self._class.max_guest, int)
        self.assertIsInstance(self._class.price_by_night, int)
        self.assertIsInstance(self._class.latitude, float)
        self.assertIsInstance(self._class.longitude, float)
        self.assertIsInstance(self._class.amenity_ids, list)
