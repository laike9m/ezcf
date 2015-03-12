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

    def __init__(self, filepath=''):
        self.filepath = filepath
        f = inspect.currentframe().f_back.f_back
        # get file location of which calls 'import'
        caller_file_location = os.path.realpath(f.f_locals['__file__'])
        print(caller_file_location)
        return


    def find_module(self, fullname, path=None):
        raise NotImplementedError()


class BaseLoader(_BaseClass):

    def __init__(self, path_entry):
        self.path_entry = path_entry

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

