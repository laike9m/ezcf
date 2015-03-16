import sys
import unittest
import os

sys.path.append('../')
import ezcf

class TestProto(unittest.TestCase):

    def test_import(self):
        import sample_config
        self.assertEqual(sample_config.hello, "world")
        self.assertEqual(sample_config.a_list, [1 ,2, 3])
        self.assertEqual(sample_config.a_dict, {
            "key1": 1000,
            "key2": ["what", 100]
        })

    def test_from_import(self):
        from sample_config import a_list, a_dict
        self.assertEqual(a_list, [1 ,2, 3])
        self.assertEqual(a_dict, {
            "key1": 1000,
            "key2": ["what", 100]
        })
        if sys.version_info[:2] > (2, 6):
            with self.assertRaises(NameError):
                print(hello)

    def test_import_as(self):
        import sample_config as config
        self.assertEqual(config.hello, "world")
        self.assertEqual(config.a_list, [1 ,2, 3])
        self.assertEqual(config.a_dict, {
            "key1": 1000,
            "key2": ["what", 100]
        })

    def test_from_import_as(self):
        from sample_config import hello as h
        from sample_config import a_list as al
        from sample_config import a_dict as ad
        self.assertEqual(h, "world")
        self.assertEqual(al, [1 ,2, 3])
        self.assertEqual(ad, {
            "key1": 1000,
            "key2": ["what", 100]
        })

    def test_import_subdir(self):
        import subdir.sample_config
        self.assertEqual(subdir.sample_config.hello, "world")
        self.assertEqual(subdir.sample_config.a_list, [1 ,2, 3])
        self.assertEqual(subdir.sample_config.a_dict, {
            "key1": 1000,
            "key2": ["what", 100]
        })

    def test_from_import_subdir(self):
        from subdir.sample_config import a_list, a_dict
        self.assertEqual(a_list, [1 ,2, 3])
        self.assertEqual(a_dict, {
            "key1": 1000,
            "key2": ["what", 100]
        })
        if sys.version_info[:2] > (2, 6):
            with self.assertRaises(NameError):
                print(hello)

    def test_import_as_subdir(self):
        import subdir.sample_config as config
        self.assertEqual(config.hello, "world")
        self.assertEqual(config.a_list, [1 ,2, 3])
        self.assertEqual(config.a_dict, {
            "key1": 1000,
            "key2": ["what", 100]
        })

    def test_from_import_as_subdir(self):
        from subdir.sample_config import hello as h
        from subdir.sample_config import a_list as al
        from subdir.sample_config import a_dict as ad
        self.assertEqual(h, "world")
        self.assertEqual(al, [1 ,2, 3])
        self.assertEqual(ad, {
            "key1": 1000,
            "key2": ["what", 100]
        })
