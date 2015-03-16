import sys
import unittest

sys.path.append('../')
import ezcf

from sample_config import *

class TestProto(unittest.TestCase):

    def test_import_all(self):
        self.assertEqual(hello, "world")
        self.assertEqual(a_list, [1 ,2, 3])
        self.assertEqual(a_dict, {
            "key1": 1000,
            "key2": ["what", 100]
        })
