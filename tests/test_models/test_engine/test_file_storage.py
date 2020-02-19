#!/usr/bin/python3
""" Tests for class FileStorage """

import unittest
from models.engine.file_storage import FileStorage
import os
import json


class TestFileStorage(unittest.TestCase):
    """ FileStorage Tests """

    def tearDown(self):
        """Removes file after running save"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_attributes(self):
        """ Tests class attributes """
        self._class = FileStorage
        self._name = "FileStorage"
        base = self._class()
        self.assertFalse(os.path.exists("file.json"))
        self.assertIsInstance(base.all(), dict)

    def test_all(self):
        """ Tests all method """

        pass

    def test_new(self):
        """ Tests new method """

        pass

    def test_save(self):
        """ Tests save method """

        pass

    def test_reload(self):
        """ Tests reload method """

        pass
