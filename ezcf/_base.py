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

    @staticmethod
    def get_parent(path, level=1):
        for _ in range(level):
            path = os.path.dirname(path)
        return path

    def get_cfg_filepath(self, fullname):
        # get file location of which calls 'import'
        caller_frame = sys._getframe(3)
        file = inspect.getfile(caller_frame)
        caller_file_dir = os.path.dirname(file)
        if '__name__' in caller_frame.f_globals:
            if '.' in caller_frame.f_globals['__name__']:  # find top packge
                up_level = len(caller_frame.f_globals['__name__'].split('.'))
                caller_file_dir = self.get_parent(caller_file_dir, up_level-1)

        if '.' in fullname:
            fullname = os.path.join(*([caller_file_dir] + fullname.split('.')))

        return fullname, caller_file_dir


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

