__author__ = 'laike9m'
__title__ = 'ezcf'
__version__ = '0.0.1'
# __build__ = None
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2015 laike9m'

import sys
from type_json import JsonFinder

sys.meta_path.append(JsonFinder())


