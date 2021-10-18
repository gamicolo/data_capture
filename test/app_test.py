#!/usr/bin/python3

import unittest
from unittest import mock
import sys
sys.path.append('../src')
from app import DataCapture, Stats 

class TestDataCapture(unittest.TestCase):

    def setUp(self):

        self.dc = DataCapture()
        self.dc.add(3)
        self.dc.add(9)
        self.dc.add(3)
        self.dc.add(4)
        self.dc.add(6)

        self.dc_sorted = DataCapture()
        self.dc_sorted.add(3)
        self.dc_sorted.add(3)
        self.dc_sorted.add(4)
        self.dc_sorted.add(6)
        self.dc_sorted.add(9)

    def test_add(self):

        dc = DataCapture()
        dc.add(1)

        self.assertEqual(dc.get_collection(),[1])

    def test_add_string(self):

        dc = DataCapture()
        dc.add('a')

        self.assertEqual(dc.get_collection(),[])

    def test_get_next_less_item_value(self):

        self.assertEqual(self.dc_sorted._get_next_less_item_value(5),4)

    def test_get_next_less_item_value_empty(self):

        self.assertEqual(self.dc_sorted._get_next_less_item_value(2),0)

    def test_get_next_greater_item_value(self):

        self.assertEqual(self.dc_sorted._get_next_greater_item_value(3),3)

    def test_get_next_greater_item_value_1(self):

        self.assertEqual(self.dc_sorted._get_next_greater_item_value(7),6)

    def test_build_stats(self):

        expected_less_values = {0:0,1:0,2:0,3:0,4:2,5:3,6:3,7:4,8:4,9:4}
        expected_greater_values = {0:5,1:5,2:5,3:3,4:2,5:2,6:1,7:1,8:1,9:0}
        stats = self.dc.build_stats()
        self.assertEqual(stats.less_values,expected_less_values)
        self.assertEqual(stats.greater_values,expected_greater_values)

class TestStats(unittest.TestCase):

    def setUp(self):

        self.stats = Stats([3,9,3,4,6], {0:0,1:0,2:0,3:0,4:2,5:3,6:3,7:4,8:4,9:4}, {0:5,1:5,2:5,3:3,4:2,5:2,6:1,7:1,8:1,9:0})

    def test_less(self):

        self.assertEqual(self.stats.less(4),2)

    def test_less_1(self):

        self.assertEqual(self.stats.less(10),5)

    def test_less_2(self):

        self.assertEqual(self.stats.less(3),0)

    def test_between(self):

        self.assertEqual(self.stats.between(3,6),4)

    def test_greater(self):

        self.assertEqual(self.stats.greater(4),2)

if __name__ == "__main__":

    unittest.main()
