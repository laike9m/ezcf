__author__ = "laike9m (laike9m@gmail.com)"
__title__ = 'ezcf'
__version__ = '0.0.1'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 laike9m'

import sys
from .api import ConfigFinder

sys.meta_path.append(ConfigFinder())