# coding: utf-8

import datetime
import sys
import unittest

sys.path.append('../../')
import ezcf


class TestProto(unittest.TestCase):

    def test_import(self):
        from .. import sample_json
        self.assertEqual(sample_json.hello, "world")
        self.assertEqual(sample_json.a_list, [1 ,2, 3])
        self.assertEqual(sample_json.a_dict, {
            "key1": 1000,
            "key2": [u"你好", 100]
        })
        from .. import sample_yaml
        self.assertEqual(sample_yaml.Date,
                         datetime.datetime(2001, 11, 23, 20, 3, 17))
        self.assertEqual(sample_yaml.Fatal, 'Unknown variable "bar"')
        self.assertEqual(
            sample_yaml.Stack,
            [{'code': 'x = MoreObject("345\\n")\n',
              'file': 'TopClass.py',
              'line': 23},
             {'code': 'foo = bar', 'file': 'MoreClass.py', 'line': 58}])
        self.assertEqual(sample_yaml.Time,
                         datetime.datetime(2001, 11, 23, 20, 2, 31))
        self.assertEqual(sample_yaml.User, 'ed')
        self.assertEqual(sample_yaml.warning,
                         u'一个 slightly different error message.')

    def test_from_import(self):
        from ..sample_json import a_list, a_dict
        self.assertEqual(a_list, [1 ,2, 3])
        self.assertEqual(a_dict, {
            "key1": 1000,
            "key2": [u"你好", 100]
        })
        from ..sample_yaml import Date, Fatal, Stack, Time, User
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

        if sys.version_info[:2] > (2, 6):
            with self.assertRaises(NameError):
                print(hello)
            with self.assertRaises(NameError):
                print(warning)

    def test_from_import_as(self):
        from ..sample_json import hello as h
        from ..sample_json import a_list as al
        from ..sample_json import a_dict as ad
        self.assertEqual(h, "world")
        self.assertEqual(al, [1 ,2, 3])
        self.assertEqual(ad, {
            "key1": 1000,
            "key2": [u"你好", 100]
        })
        from ..sample_yaml import Date as d
        from ..sample_yaml import Fatal as f
        from ..sample_yaml import Stack as s
        from ..sample_yaml import Time as t
        from ..sample_yaml import User as u
        from ..sample_yaml import warning as w
        self.assertEqual(d, datetime.datetime(2001, 11, 23, 20, 3, 17))
        self.assertEqual(f, 'Unknown variable "bar"')
        self.assertEqual(
            s,
            [{'code': 'x = MoreObject("345\\n")\n',
              'file': 'TopClass.py',
              'line': 23},
             {'code': 'foo = bar', 'file': 'MoreClass.py', 'line': 58}])
        self.assertEqual(t, datetime.datetime(2001, 11, 23, 20, 2, 31))
        self.assertEqual(u, 'ed')
        self.assertEqual(w, u'一个 slightly different error message.')
