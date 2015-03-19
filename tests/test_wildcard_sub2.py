# coding: utf-8

import datetime
import sys
import unittest

sys.path.append('../')
import ezcf

from subdir.subdir.sample_json import *
from subdir.subdir.sample_yaml import *


class TestProto(unittest.TestCase):

    def test_import_all(self):
        self.assertEqual(hello, "world")
        self.assertEqual(a_list, [1 ,2, 3])
        self.assertEqual(a_dict, {
            "key1": 1000,
            "key2": [u"你好", 100]
        })
        self.assertEqual(Date, datetime.datetime(2001, 11, 23, 20, 3, 17))
        self.assertEqual(Fatal, 'Unknown variable "bar"')
        self.assertEqual(
            Stack,
            [{'code': 'x = MoreObject("345\\n")\n',
              'file': 'TopClass.py',
              'line': 23},
             {'code': 'foo = bar', 'file': 'MoreClass.py', 'line': 58}])
        self.assertEqual(Time, datetime.datetime(2001, 11, 23, 20, 2, 31))
        self.assertEqual(User, 'ed')
        self.assertEqual(warning, 'A slightly different error message.')
