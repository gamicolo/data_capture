#!/usr/bin/python3

import unittest
from unittest import mock
import sys
sys.path.append('../src')
from main import DataCapture, Stats 

class TestDataCapture(unittest.TestCase):

    def setUp(self):

        pass

    def test_add(self):

        dc = DataCapture()
        dc.add(1)

        self.assertEqual(dc.get_collection(),[1])

    def test_add_string(self):

        dc = DataCapture()
        dc.add('a')

        self.assertEqual(dc.get_collection(),[])

class TestStats(unittest.TestCase):

    def setUp(self):

        self.stats = Stats([3,9,3,4,6])

    def test_less(self):

        self.assertEqual(self.stats.less(4),2)

    def test_between(self):

        self.assertEqual(self.stats.between(3,6),4)

    def test_greater(self):

        self.assertEqual(self.stats.greater(4),2)

if __name__ == "__main__":

    unittest.main()
