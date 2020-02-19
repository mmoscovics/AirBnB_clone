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

    def tearDown(self):
        """Removes file after running save"""
        try:
            os.remove("file.JSON")
        except Exception:
            pass

    def test_id(self):
        """ Test id """

        base = self._class()
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(UUID(base.id), UUID)

    def test_created_at(self):
        """ Tests created_at """

        base = self._class()
        now = dt.now()
        self.assertIsInstance(base.created_at, dt)
        self.assertIsInstance(base.updated_at, dt)
        self.assertTrue(now >= base.created_at)
        self.assertTrue(now >= base.updated_at)

    def test_updated_at(self):
        """ Tests updated_at """

        base = self._class()
        now = base.updated_at
        self.assertIsInstance(base.updated_at, dt)
        base.updated_at = dt.now

    def test_str(self):
        """ Tests __str__ """

        base = self._class()
        form = '[' + self._name + "] ({}) {}".format(
            base.id, str(base.__dict__))
        self.assertEqual(str(base), form)

    def test_to_dict(self):
        """ Tests to_dict """

        base = self._class()
        obj_dict = base.to_dict()
        key = set(obj_dict.keys())
        key2 = set(base.__dict__.keys())
        self.assertTrue(key2.issubset(key))
        self.assertTrue("__class__" in key)
        self.assertEqual(obj_dict["__class__"], self._name)
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertEqual(obj_dict["created_at"], base.created_at.isoformat())
        self.assertIsInstance(obj_dict["updated_at"], str)
        self.assertEqual(obj_dict["updated_at"], base.updated_at.isoformat())

    def test_save(self):
        """ Tests save """

        if os.path.exists("file.json"):
            os.remove("file.json")
        FileStorage.reload()
        base = self._class()
        self.assertTrue(self._name + '.' + base.id in FileStorage.all())

    def test_from_dict(self):
        """ Tests from dictionary """

        pass
