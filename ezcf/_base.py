"""
Base Finder and Loader Class
"""

import imp
import inspect
import os
import sys

class FileNotFoundError(Exception):
    pass


class _BaseClass(object):
    pass


class BaseFinder(_BaseClass):

    def __init__(self, *args, **kwargs):
        # get file location of which calls 'import'
        file = inspect.getfile(sys._getframe(3))
        self.dir = os.path.dirname(file)
        return

    def find_module(self, fullname, path=None):
        raise NotImplementedError()


class BaseLoader(_BaseClass):

    def __init__(self, dir):
        self.dir = dir

    def load_module(self, fullname):
        if fullname in sys.modules:
            mod = sys.modules[fullname]
        else:
            mod = sys.modules.setdefault(fullname, imp.new_module(fullname))

        mod.__file__ = fullname
        mod.__name__ = fullname
        mod.__loader__ = self
        mod.__package__ = '.'.join(fullname.split('.')[:-1])

        return mod

