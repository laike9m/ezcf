__author__ = "laike9m (laike9m@gmail.com)"
__title__ = 'ezcf'
__version__ = '0.0.1'
# __build__ = None
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2015 laike9m'

import sys
from .type_json import JsonFinder
from .type_yaml import YamlFinder

sys.meta_path.append(JsonFinder())
sys.meta_path.append(YamlFinder())


