import os
import unittest
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from subdir.subdir.test_parent import *

if __name__ == '__main__':
    unittest.main()