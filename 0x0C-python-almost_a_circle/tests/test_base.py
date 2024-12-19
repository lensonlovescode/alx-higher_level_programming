#!/usr/bin/python3
"""
This module contains unit tests for the Base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id_assignment(self):
        """ Test that ids are assigned correctly """
        b1 = Base()
        b2 = Base()
        b3 = Base(5)
        
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 5)

    def test_to_json_string(self):
        """ Test the to_json_string method """
        dict_list = [{'id': 1}, {'id': 2}]
        json_string = Base.to_json_string(dict_list)
        self.assertEqual(json_string, '[{"id": 1}, {"id": 2}]')
        
        # Test empty list
        self.assertEqual(Base.to_json_string([]), '[]')
        # Test None
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_from_json_string(self):
        """ Test the from_json_string method """
        json_string = '[{"id": 1}, {"id": 2}]'
        dict_list = Base.from_json_string(json_string)
        self.assertEqual(dict_list, [{'id': 1}, {'id': 2}])
        
        # Test empty string
        self.assertEqual(Base.from_json_string(''), [])
        # Test None
        self.assertEqual(Base.from_json_string(None), [])

    def test_save_to_file(self):
        """ Test save_to_file method """
        b1 = Base(1)
        b2 = Base(2)
        list_objs = [b1, b2]

        Base.save_to_file(list_objs)

        # Check if the file is created and has correct content
        with open("Base.json", 'r') as f:
            content = f.read()
            self.assertIn('"id": 1', content)
            self.assertIn('"id": 2', content)

    def test_load_from_file(self):
        """ Test load_from_file method """
        b1 = Base(1)
        b2 = Base(2)
        list_objs = [b1, b2]

        Base.save_to_file(list_objs)
        loaded_objs = Base.load_from_file()

        self.assertEqual(len(loaded_objs), 2)
        self.assertEqual(loaded_objs[0].id, 1)
        self.assertEqual(loaded_objs[1].id, 2)

    def test_load_from_file_not_found(self):
        """ Test load_from_file when the file doesn't exist """
        self.assertEqual(Base.load_from_file(), [])


if __name__ == '__main__':
    unittest.main()

