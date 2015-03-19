# coding: utf-8

import sys
import unittest
import os
import datetime
from pprint import pprint

sys.path.append('../')
import ezcf


class TestProto(unittest.TestCase):

    def test_import(self):
        import sample_json
        self.assertEqual(sample_json.hello, "world")
        self.assertEqual(sample_json.a_list, [1 ,2, 3])
        self.assertEqual(sample_json.a_dict, {
            "key1": 1000,
            "key2": [u"你好", 100]
        })
        import sample_yaml
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
        import sample_yml
        self.assertEqual(sample_yml.Date,
                         datetime.datetime(2001, 11, 23, 20, 3, 17))
        self.assertEqual(sample_yml.Fatal, 'Unknown variable "bar"')
        self.assertEqual(
            sample_yml.Stack,
            [{'code': 'x = MoreObject("345\\n")\n',
              'file': 'TopClass.py',
              'line': 23},
             {'code': 'foo = bar', 'file': 'MoreClass.py', 'line': 58}])
        self.assertEqual(sample_yml.Time,
                         datetime.datetime(2001, 11, 23, 20, 2, 31))
        self.assertEqual(sample_yml.User, 'ed')
        self.assertEqual(sample_yml.warning,
                         'A slightly different error message.')

    def test_from_import(self):
        from sample_json import a_list, a_dict
        self.assertEqual(a_list, [1 ,2, 3])
        self.assertEqual(a_dict, {
            "key1": 1000,
            "key2": [u"你好", 100]
        })
        from sample_yaml import Date, Fatal, Stack, Time, User
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

    def test_import_as(self):
        import sample_json as sj
        self.assertEqual(sj.hello, "world")
        self.assertEqual(sj.a_list, [1 ,2, 3])
        self.assertEqual(sj.a_dict, {
            "key1": 1000,
            "key2": [u"你好", 100]
        })
        import sample_yaml as sy
        self.assertEqual(sy.Date, datetime.datetime(2001, 11, 23, 20, 3, 17))
        self.assertEqual(sy.Fatal, 'Unknown variable "bar"')
        self.assertEqual(
            sy.Stack,
             [{'code': 'x = MoreObject("345\\n")\n',
               'file': 'TopClass.py',
               'line': 23},
              {'code': 'foo = bar', 'file': 'MoreClass.py', 'line': 58}])
        self.assertEqual(sy.Time, datetime.datetime(2001, 11, 23, 20, 2, 31))
        self.assertEqual(sy.User, 'ed')
        self.assertEqual(sy.warning, u'一个 slightly different error message.')

    def test_from_import_as(self):
        from sample_json import hello as h
        from sample_json import a_list as al
        from sample_json import a_dict as ad
        self.assertEqual(h, "world")
        self.assertEqual(al, [1 ,2, 3])
        self.assertEqual(ad, {
            "key1": 1000,
            "key2": [u"你好", 100]
        })
        from sample_yaml import Date as d
        from sample_yaml import Fatal as f
        from sample_yaml import Stack as s
        from sample_yaml import Time as t
        from sample_yaml import User as u
        from sample_yaml import warning as w
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

    def test_import_subdir(self):
        import subdir.sample_json
        self.assertEqual(subdir.sample_json.hello, "world")
        self.assertEqual(subdir.sample_json.a_list, [1 ,2, 3])
        self.assertEqual(subdir.sample_json.a_dict, {
            "key1": 1000,
            "key2": [u"你好", 100]
        })
        import subdir.sample_yaml
        self.assertEqual(subdir.sample_yaml.Date,
                         datetime.datetime(2001, 11, 23, 20, 3, 17))
        self.assertEqual(subdir.sample_yaml.Fatal, 'Unknown variable "bar"')
        self.assertEqual(
            subdir.sample_yaml.Stack,
            [{'code': 'x = MoreObject("345\\n")\n',
              'file': 'TopClass.py',
              'line': 23},
             {'code': 'foo = bar', 'file': 'MoreClass.py', 'line': 58}])
        self.assertEqual(subdir.sample_yaml.Time,
                         datetime.datetime(2001, 11, 23, 20, 2, 31))
        self.assertEqual(subdir.sample_yaml.User, 'ed')
        self.assertEqual(subdir.sample_yaml.warning,
                         'A slightly different error message.')


    def test_from_import_subdir(self):
        from subdir.sample_json import a_list, a_dict
        self.assertEqual(a_list, [1 ,2, 3])
        self.assertEqual(a_dict, {
            "key1": 1000,
            "key2": [u"你好", 100]
        })
        from subdir.sample_yaml import Date, Fatal, Stack, Time, User
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

    def test_import_as_subdir(self):
        import subdir.sample_json as sj
        self.assertEqual(sj.hello, "world")
        self.assertEqual(sj.a_list, [1 ,2, 3])
        self.assertEqual(sj.a_dict, {
            "key1": 1000,
            "key2": [u"你好", 100]
        })
        import subdir.sample_yaml as sy
        self.assertEqual(sy.Date, datetime.datetime(2001, 11, 23, 20, 3, 17))
        self.assertEqual(sy.Fatal, 'Unknown variable "bar"')
        self.assertEqual(
            sy.Stack,
             [{'code': 'x = MoreObject("345\\n")\n',
               'file': 'TopClass.py',
               'line': 23},
              {'code': 'foo = bar', 'file': 'MoreClass.py', 'line': 58}])
        self.assertEqual(sy.Time, datetime.datetime(2001, 11, 23, 20, 2, 31))
        self.assertEqual(sy.User, 'ed')
        self.assertEqual(sy.warning, 'A slightly different error message.')

    def test_from_import_as_subdir(self):
        from subdir.sample_json import hello as h
        from subdir.sample_json import a_list as al
        from subdir.sample_json import a_dict as ad
        self.assertEqual(h, "world")
        self.assertEqual(al, [1 ,2, 3])
        self.assertEqual(ad, {
            "key1": 1000,
            "key2": [u"你好", 100]
        })
        from subdir.sample_yaml import Date as d
        from subdir.sample_yaml import Fatal as f
        from subdir.sample_yaml import Stack as s
        from subdir.sample_yaml import Time as t
        from subdir.sample_yaml import User as u
        from subdir.sample_yaml import warning as w
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
        self.assertEqual(w, 'A slightly different error message.')

    def test_import_subdir2(self):
        import subdir.subdir.sample_json
        self.assertEqual(subdir.subdir.sample_json.hello, "world")
        self.assertEqual(subdir.subdir.sample_json.a_list, [1 ,2, 3])
        self.assertEqual(subdir.subdir.sample_json.a_dict, {
            "key1": 1000,
            "key2": [u"你好", 100]
        })
        import subdir.subdir.sample_yaml
        self.assertEqual(subdir.subdir.sample_yaml.Date,
                         datetime.datetime(2001, 11, 23, 20, 3, 17))
        self.assertEqual(subdir.subdir.sample_yaml.Fatal,
                         'Unknown variable "bar"')
        self.assertEqual(
            subdir.subdir.sample_yaml.Stack,
             [{'code': 'x = MoreObject("345\\n")\n',
               'file': 'TopClass.py',
               'line': 23},
              {'code': 'foo = bar', 'file': 'MoreClass.py', 'line': 58}])
        self.assertEqual(subdir.subdir.sample_yaml.Time,
                         datetime.datetime(2001, 11, 23, 20, 2, 31))
        self.assertEqual(subdir.subdir.sample_yaml.User, 'ed')
        self.assertEqual(subdir.subdir.sample_yaml.warning,
                         'A slightly different error message.')

    def test_from_import_subdir2(self):
        from subdir.subdir.sample_json import a_list, a_dict
        self.assertEqual(a_list, [1 ,2, 3])
        self.assertEqual(a_dict, {
            "key1": 1000,
            "key2": [u"你好", 100]
        })
        from subdir.subdir.sample_yaml import Date, Fatal, Stack, Time, User
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

    def test_import_as_subdir2(self):
        import subdir.subdir.sample_json as config
        self.assertEqual(config.hello, "world")
        self.assertEqual(config.a_list, [1 ,2, 3])
        self.assertEqual(config.a_dict, {
            "key1": 1000,
            "key2": [u"你好", 100]
        })
        import subdir.subdir.sample_yaml as sy
        self.assertEqual(sy.Date, datetime.datetime(2001, 11, 23, 20, 3, 17))
        self.assertEqual(sy.Fatal, 'Unknown variable "bar"')
        self.assertEqual(
            sy.Stack,
            [{'code': 'x = MoreObject("345\\n")\n',
              'file': 'TopClass.py',
              'line': 23},
             {'code': 'foo = bar', 'file': 'MoreClass.py', 'line': 58}])
        self.assertEqual(sy.Time, datetime.datetime(2001, 11, 23, 20, 2, 31))
        self.assertEqual(sy.User, 'ed')
        self.assertEqual(sy.warning, 'A slightly different error message.')

    def test_from_import_as_subdir2(self):
        from subdir.sample_json import hello as h
        from subdir.subdir.sample_json import a_list as al
        from subdir.subdir.sample_json import a_dict as ad
        self.assertEqual(h, "world")
        self.assertEqual(al, [1 ,2, 3])
        self.assertEqual(ad, {
            "key1": 1000,
            "key2": [u"你好", 100]
        })
        from subdir.subdir.sample_yaml import Date as d
        from subdir.subdir.sample_yaml import Fatal as f
        from subdir.subdir.sample_yaml import Stack as s
        from subdir.subdir.sample_yaml import Time as t
        from subdir.subdir.sample_yaml import User as u
        from subdir.subdir.sample_yaml import warning as w
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
        self.assertEqual(w, 'A slightly different error message.')

    def test_invalid_json(self):
        from ezcf._base import InvalidJsonError
        if sys.version_info[:2] > (2, 6):
            with self.assertRaises(InvalidJsonError):
                import invalid_json

    def test_invalid_yaml(self):
        from ezcf._base import InvalidYamlError
        if sys.version_info[:2] > (2, 6):
            with self.assertRaises(InvalidYamlError):
                import invalid_yaml
