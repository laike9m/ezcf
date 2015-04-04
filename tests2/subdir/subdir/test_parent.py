# coding: utf-8

import datetime
import sys
import unittest

import ezcf


class TestProto(unittest.TestCase):

    def test_import(self):
        from .. import sample_json
        self.assertEqual(sample_json.hello, "world")
        self.assertEqual(sample_json.a_list, [1, 2, 3])
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
        from .. import sample_ini
        self.assertEqual(sample_ini.keyword1, 'value1')
        self.assertEqual(sample_ini.keyword2, 'value2')
        self.assertDictEqual(
            sample_ini.section1,
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
        self.assertDictEqual(sample_ini.section2,
                             {'keyword1': 'value1', 'keyword2': 'value2'})

    def test_from_import(self):
        from ..sample_json import a_list, a_dict
        self.assertEqual(a_list, [1, 2, 3])
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
        from ..sample_ini import keyword1
        from ..sample_ini import section1
        from ..sample_ini import section2
        self.assertEqual(keyword1, 'value1')
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

        if sys.version_info[:2] > (2, 6):
            with self.assertRaises(NameError):
                print(hello)
            with self.assertRaises(NameError):
                print(warning)
            with self.assertRaises(NameError):
                print(keyword2)

    def test_from_import_as(self):
        from ..sample_json import hello as h
        from ..sample_json import a_list as al
        from ..sample_json import a_dict as ad
        self.assertEqual(h, "world")
        self.assertEqual(al, [1, 2, 3])
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
        from ..sample_ini import keyword1 as k1
        from ..sample_ini import keyword2 as k2
        from ..sample_ini import section1 as s1
        from ..sample_ini import section2 as s2
        self.assertEqual(k1, 'value1')
        self.assertEqual(k2, 'value2')
        self.assertDictEqual(s1, {
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
        self.assertDictEqual(s2, {'keyword1': 'value1', 'keyword2': 'value2'})
