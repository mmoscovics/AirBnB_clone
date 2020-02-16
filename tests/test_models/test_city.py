#!/usr/bin/python3
""" Tests for class City """

import unittest
from models.base_model import BaseModel
from models.city import City
from tests.test_models.test_base_model import TestBaseModel


class TestCity(TestBaseModel):
    """ City Tests """

    def __init__(self, *args, **kwargs):
        """ Constructor attributes and objects to test """

        super()__init__(*args, **kwargs)
        self._class = City
        self._name = "City"
