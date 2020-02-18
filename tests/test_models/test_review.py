#!/usr/bin/python3
""" Tests for class Review """

import unittest
from models.base_model import BaseModel
from models.review import Review
from tests.test_models.test_base_model import TestBaseModel


class TestReview(TestBaseModel):
    """ Review Tests """

    def __init__(self, *args, **kwargs):
        """ Constructor attributes and objects to test """

        super().__init__(*args, **kwargs)
        self._class = Review
        self._name = "Review"

    def test__class_attrs(self):
        """ Test for attributes """

        self.assertIsInstance(self._class.place_id, str)
        self.assertIsInstance(self._class.user_id, str)
        self.assertIsInstance(self._class.text, str)
