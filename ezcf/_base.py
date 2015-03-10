"""
Base Finder and Loader Class
"""

import sys
import imp

class FileNotFoundError(Exception):
    pass


class BaseFinder():

    def __init__(self, filepath=''):
        self.filepath = filepath
        return

    def find_module(self):
        raise NotImplementedError()


class BaseLoader():

    def __init__(self, path_entry):
        self.path_entry = path_entry

    def load_module(self, fullname):
        if fullname in sys.modules:
            mod = sys.modules[fullname]
        else:
            mod = sys.modules.setdefault(fullname, imp.new_module(fullname))

        mod.__file__ = fullname
        mod.__name__ = fullname
        mod.__path__ = ['path-entry-goes-here']
        mod.__loader__ = self
        mod.__package__ = '.'.join(fullname.split('.')[:-1])

        return mod

