#!/usr/bin/python3
""" Tests for class State """

import unittest
from models.base_model import BaseModel
from models.state import State
from tests.test_models.test_base_model import TestBaseModel


class TestState(TestBaseModel):
    """ State Tests """

    def __init__(self, *args, **kwargs):
        """ Constructor attributes and objects to test """

        super().__init__(*args, **kwargs)
        self._class = State
        self._name = "State"
