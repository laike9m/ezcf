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
        caller_frame = sys._getframe(3)
        file = inspect.getfile(caller_frame)  # file that calls 'import '
        top_package_dir = os.path.dirname(file)
        if '__name__' in caller_frame.f_globals:
            if '.' in caller_frame.f_globals['__name__']:  # find top package
                up_level = len(caller_frame.f_globals['__name__'].split('.'))
                top_package_dir = self.get_parent(top_package_dir, up_level-1)

        if '.' in fullname:
            cfg_file = os.path.join(*([top_package_dir] + fullname.split('.')))
        else:
            cfg_file = fullname

        return cfg_file


class BaseLoader(_BaseClass):

    def __init__(self, *args, **kwargs):
        pass

    def load_module(self, fullname):
        if fullname in sys.modules:
            mod = sys.modules[fullname]
        else:
            mod = sys.modules.setdefault(fullname, imp.new_module(fullname))

        mod.__file__ = self.cfg_file
        mod.__name__ = fullname
        mod.__loader__ = self
        mod.__package__ = '.'.join(fullname.split('.')[:-1])

        return mod

