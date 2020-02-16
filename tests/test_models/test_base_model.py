#!/usr/bin/python3
""" Tests for class BaseModel """

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from uuid import UUID
from datetime import datetime as dt
import os


class TestBaseModel(unittest.TestCase):
    """ BaseModel Tests """

    def __init__(self, *args, **kwargs):
        """ Constructor attributes and objects to test """

        super().__init__(*args, **kwargs)
        self._class = BaseModel
        self._name = "BaseModel"

    def test_id(self):
        """ Test id """

        base = self.test_class()
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(UUID(base.id), UUID)
