#!/usr/bin/python3
""" Tests for class User """

import unittest
from models.base_model import BaseModel
from models.user import User
from tests.test_models.test_base_model import TestBaseModel


class TestUser(TestBaseModel):
    """ User Tests """

    def __init__(self, *args, **kwargs):
        """ Constructor attributes and objects to test """

        super()__init__(*args, **kwargs)
        self._class = User
        self._name = "User"
