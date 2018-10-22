#!/usr/bin/python3
"""Unittest for class base)
"""
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """class for Test Base"""
    @classmethod
    def setUpClass(cls):
        """set up the instance"""
        cls.b1 = Base()
        cls.b2 = Base(12)
        cls.b3 = Base()
        cls.b4 = Base()
        cls.r1 = Rectangle(10, 7, 2, 8)
        cls.r2 = Rectangle(10, 7, 2, 8)
        cls.r3 = Rectangle(2, 4)
        cls.r4 = Rectangle(3, 5, 1)
        r4_dictionary = cls.r4.to_dictionary()
        cls.r5 = Rectangle.create(**r4_dictionary)
        cls.s1 = Square(5)
        cls.s2 = Square(7, 9, 1)

    @classmethod
    def tearDownCass(cls):
        """tear down"""
        pass

    def testId1(self):
        """test Id only"""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 12)
        self.assertEqual(self.b3.id, 2)
        self.assertEqual(self.b4.id, 3)

    def test_json_dict_to_str_0(self):
        """test json, convert dict to str"""
        dictionary = self.r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(dictionary, {'x': 2, 'width': 10,
                                      'id': 4, 'height': 7, 'y': 8})
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(sorted(json_dictionary),
                         sorted('[{"height": 7, "x": 2, "width": '
                                '10, "y": 8, "id": 4}]'))
        self.assertEqual(type(json_dictionary), str)

    def test_json_str_to_file_0(self):
        """test json, str to file"""
        ret_dic = []
        Rectangle.save_to_file([self.r2, self.r3])
        with open("Rectangle.json", "r") as file:
            string = file.read()
        self.assertEqual(sorted(string), sorted(
                '[{"y": 8, "x": 2, "id": 5, "width": 10, "height": 7}, '
                '{"y": 0, "x": 0, "id": 6, "width": 2, "height": 4}]'))

    def test_json_str_to_dic_1(self):
        """test json, str to dictionary"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10,
                                        'id': 89}, {'height': 7, 'width': 1,
                                                    'id': 7}])

    def test_json_create_1(self):
        """json create"""
        self.assertEqual(self.r5.__str__(), '[Rectangle] (7) 1/0 - 3/5')

    def test_json_load_file(self):
        """json load file"""
        list_rectangles_input = [self.r2, self.r3]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEquals([obj.__dict__ for obj in list_rectangles_input],
                          [obj.__dict__ for obj in list_rectangles_output])

    def test_csv_1(self):
        """test csv1"""
        list_rectangles_input = [self.r2, self.r3]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        for rect in list_rectangles_output:
            self.assertEquals(rect.__str__(), '[Rectangle] ({}) {}/{} - {}/{}'
                              .format(rect.id, rect.x, rect.y, rect.width,
                                      rect.height))

    def test_csv_2(self):
        """test csv2"""
        print(self.s1.id, self.s2.id)
        list_squares_input = [self.s1, self.s2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        for rect in list_squares_output:
            self.assertEquals(rect.__str__(), '[Square] ({}) {}/{} - {}'
                              .format(rect.id, rect.x, rect.y, rect.size))

if __name__ == '__main__':
    unittest.main()
