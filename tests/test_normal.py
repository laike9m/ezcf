import sys
import unittest
import os

sys.path.append('../')
import ezcf

class TestProto(unittest.TestCase):

    def test_import(self):
        import sample_json
        self.assertEqual(sample_json.hello, "world")
        self.assertEqual(sample_json.a_list, [1 ,2, 3])
        self.assertEqual(sample_json.a_dict, {
            "key1": 1000,
            "key2": ["what", 100]
        })

    def test_from_import(self):
        from sample_json import a_list, a_dict
        self.assertEqual(a_list, [1 ,2, 3])
        self.assertEqual(a_dict, {
            "key1": 1000,
            "key2": ["what", 100]
        })
        if sys.version_info[:2] > (2, 6):
            with self.assertRaises(NameError):
                print(hello)

    def test_import_as(self):
        import sample_json as config
        self.assertEqual(config.hello, "world")
        self.assertEqual(config.a_list, [1 ,2, 3])
        self.assertEqual(config.a_dict, {
            "key1": 1000,
            "key2": ["what", 100]
        })

    def test_from_import_as(self):
        from sample_json import hello as h
        from sample_json import a_list as al
        from sample_json import a_dict as ad
        self.assertEqual(h, "world")
        self.assertEqual(al, [1 ,2, 3])
        self.assertEqual(ad, {
            "key1": 1000,
            "key2": ["what", 100]
        })

    def test_import_subdir(self):
        import subdir.sample_json
        self.assertEqual(subdir.sample_json.hello, "world")
        self.assertEqual(subdir.sample_json.a_list, [1 ,2, 3])
        self.assertEqual(subdir.sample_json.a_dict, {
            "key1": 1000,
            "key2": ["what", 100]
        })

    def test_from_import_subdir(self):
        from subdir.sample_json import a_list, a_dict
        self.assertEqual(a_list, [1 ,2, 3])
        self.assertEqual(a_dict, {
            "key1": 1000,
            "key2": ["what", 100]
        })
        if sys.version_info[:2] > (2, 6):
            with self.assertRaises(NameError):
                print(hello)

    def test_import_as_subdir(self):
        import subdir.sample_json as config
        self.assertEqual(config.hello, "world")
        self.assertEqual(config.a_list, [1 ,2, 3])
        self.assertEqual(config.a_dict, {
            "key1": 1000,
            "key2": ["what", 100]
        })

    def test_from_import_as_subdir(self):
        from subdir.sample_json import hello as h
        from subdir.sample_json import a_list as al
        from subdir.sample_json import a_dict as ad
        self.assertEqual(h, "world")
        self.assertEqual(al, [1 ,2, 3])
        self.assertEqual(ad, {
            "key1": 1000,
            "key2": ["what", 100]
        })

    def test_import_subdir2(self):
        import subdir.subdir.sample_json
        self.assertEqual(subdir.subdir.sample_json.hello, "world")
        self.assertEqual(subdir.subdir.sample_json.a_list, [1 ,2, 3])
        self.assertEqual(subdir.subdir.sample_json.a_dict, {
            "key1": 1000,
            "key2": ["what", 100]
        })

    def test_from_import_subdir2(self):
        from subdir.subdir.sample_json import a_list, a_dict
        self.assertEqual(a_list, [1 ,2, 3])
        self.assertEqual(a_dict, {
            "key1": 1000,
            "key2": ["what", 100]
        })
        if sys.version_info[:2] > (2, 6):
            with self.assertRaises(NameError):
                print(hello)

    def test_import_as_subdir2(self):
        import subdir.subdir.sample_json as config
        self.assertEqual(config.hello, "world")
        self.assertEqual(config.a_list, [1 ,2, 3])
        self.assertEqual(config.a_dict, {
            "key1": 1000,
            "key2": ["what", 100]
        })

    def test_from_import_as_subdir2(self):
        from subdir.sample_json import hello as h
        from subdir.subdir.sample_json import a_list as al
        from subdir.subdir.sample_json import a_dict as ad
        self.assertEqual(h, "world")
        self.assertEqual(al, [1 ,2, 3])
        self.assertEqual(ad, {
            "key1": 1000,
            "key2": ["what", 100]
        })
