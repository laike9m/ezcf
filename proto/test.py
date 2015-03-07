import prototype
import sys
from pprint import pprint
import unittest

class TestProto(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        sys.meta_path.append(prototype.JsonImportFinder())
        import sample_config
        globals().update(sample_config.__dict__)

    def test_one(self):
        self.assertEqual(hello, "world")
