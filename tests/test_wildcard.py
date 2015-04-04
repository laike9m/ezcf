# coding: utf-8

import datetime
import sys
import unittest

try:
    import ezcf
except ImportError:
    sys.path.append('../')
    import ezcf

from sample_json import *
from sample_yaml import *
from sample_ini import *


class TestProto(unittest.TestCase):

    def test_import_all(self):
        self.assertEqual(hello, "world")
        self.assertEqual(a_list, [1, 2, 3])
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
        self.assertEqual(warning, u'一个 slightly different error message.')
        self.assertEqual(keyword1, 'value1')
        self.assertEqual(keyword2, 'value2')
        self.assertDictEqual(
            section1,
            {
                'keyword1': 'value1', 'keyword2': 'value2',
                'sub-section': {
                    'keyword1': 'value1', 'keyword2': 'value2',
                    'nested section': {
                        'keyword1': 'value1', 'keyword2': 'value2',
                        },
                    },
                'sub-section2': {
                    'keyword1': 'value1', 'keyword2': 'value2',
                    },
                }
        )
        self.assertDictEqual(section2,
                             {'keyword1': 'value1', 'keyword2': 'value2'})
