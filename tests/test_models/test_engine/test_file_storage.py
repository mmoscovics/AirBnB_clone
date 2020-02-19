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
            os.remove("file.JSON")
        except Exception:
            pass

    def test_attributes(self):
        """ Tests class attributes """

        pass

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
