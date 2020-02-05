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
