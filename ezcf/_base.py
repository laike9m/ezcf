"""
Base Finder and Loader Class
"""

import imp
import inspect
import os
import sys


class InvalidJsonError(Exception):
    pass


class InvalidYamlError(Exception):
    pass


class _BaseClass(object):
    pass


class BaseFinder(_BaseClass):

    def __init__(self, *args, **kwargs):
        pass

    def find_module(self, *args, **kwargs):
        raise NotImplementedError()

    def get_cfg_filepath(self, fullname):
        # get file location of which calls 'import'
        file = inspect.getfile(sys._getframe(3))
        dir = os.path.dirname(file)
        if '.' in fullname:
            fullname = os.path.join(*([dir] + fullname.split('.')))
        return fullname, dir


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

