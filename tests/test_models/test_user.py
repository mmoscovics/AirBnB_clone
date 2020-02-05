#!/usr/bin/python3
""" Tests for class User """

import unittest
from models.base_model import BaseModel
from models.user import User
from tests.test_models.test_base_model import TestBaseModel
from uuid import UUID
from datetime import datetime as dt

class TestUser(TestBaseModel):
    """ User Tests """

    def __init__(self, *args, **kwargs):
        """ Constructor attributes and objects to test """

        super()__init__(*args, **kwargs)
        self._class = User
        self._name = "User"

    def test_attrs(self):
    """ Test for attributes """

        self.assertIsInstance(self._class.email, str)
        self.assertIsInstance(self._class.password, str)
        self.assertIsInstance(self._class.first_name, str)
        self.assertIsInstance(self._class.last_name, str)
