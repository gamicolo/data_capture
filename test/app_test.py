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

        self.assertEqual(dc.get_numbers(),[1])

    def test_add_string(self):

        dc = DataCapture()
        dc.add('a')

        self.assertEqual(dc.get_numbers(),[])

    def test_get_same_less_and_less_equal_values(self):

        self.assertEqual(self.dc_sorted._get_less_values(5),(4,4))

    def test_get_different_less_and_less_equal_values(self):

        self.assertEqual(self.dc_sorted._get_less_values(4),(4,3))

    def test_get_less_values_with_zero_match(self):

        self.assertEqual(self.dc_sorted._get_less_values(2),(0,0))

    def test_get_less_values_with_max_match(self):

        self.assertEqual(self.dc_sorted._get_less_values(10),(9,9))

    def test_build_stats(self):

        expected_less_values = {0:0,1:0,2:0,3:0,4:2,5:3,6:3,7:4,8:4,9:4}
        expected_less_equal_values = {0:0,1:0,2:0,3:2,4:3,5:3,6:4,7:4,8:4,9:5}
        expected_greater_values = {0:5,1:5,2:5,3:3,4:2,5:2,6:1,7:1,8:1,9:0}
        stats = self.dc.build_stats()

        self.assertEqual(stats.less_values,expected_less_values)
        self.assertEqual(stats.less_equal_values,expected_less_equal_values)
        self.assertEqual(stats.greater_values,expected_greater_values)

class TestStats(unittest.TestCase):

    def setUp(self):

        self.stats = Stats([3,9,3,4,6], {0:0,1:0,2:0,3:0,4:2,5:3,6:3,7:4,8:4,9:4}, {0:0,1:0,2:0,3:2,4:3,5:3,6:4,7:4,8:4,9:5}, {0:5,1:5,2:5,3:3,4:2,5:2,6:1,7:1,8:1,9:0})

    def test_less_ok(self):

        self.assertEqual(self.stats.less(4),2)

    def test_less_not_int(self):

        self.assertEqual(self.stats.less('h'),0)

    def test_less_not_in_dict_less(self):

        self.assertEqual(self.stats.less(10),5)

    def test_less_with_zero_match(self):

        self.assertEqual(self.stats.less(3),0)

    def test_between_ok(self):

        self.assertEqual(self.stats.between(3,6),4)

    def test_between_another_ok(self):

        self.assertEqual(self.stats.between(4,9),3)

    def test_between_not_in_less_dicts(self):

        self.assertEqual(self.stats.between(10,12),0)

    def test_between_first_not_int(self):

        self.assertEqual(self.stats.between('h',6),0)

    def test_between_second_not_int(self):

        self.assertEqual(self.stats.between(3,'h'),0)

    def test_between_first_not_greater_than_second(self):

        self.assertEqual(self.stats.between(6,3),0)

    def test_greater_ok(self):

        self.assertEqual(self.stats.greater(4),2)

    def test_greater_not_in_dict_greater(self):

        self.assertEqual(self.stats.greater(10),0)

    def test_greater_not_int(self):

        self.assertEqual(self.stats.greater('h'),0)

if __name__ == "__main__":

    unittest.main()
