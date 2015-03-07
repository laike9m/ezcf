#!/usr/bin/env/python
# coding: utf-8

"""
This is a prototype to demonstrate ezcf can work on py2
"""

__author__ = "laike9m (laike9m@gmail.com)"

import sys
import imp
import os
import json


class JsonImportFinder(object):

    def __init__(self, filepath=''):
        print('Creating JsonImportFinder for %s' % filepath)
        self.filepath = filepath
        return

    def find_module(self, fullname, path=None):
        print('JsonImportFinder looking for "%s" with path "%s"' %
              (fullname, path))
        if os.path.isfile(fullname + '.json'):
            return JsonImportLoader(fullname + '.json')
        else:
            return None


class JsonImportLoader(object):

    def __init__(self, path_entry):
        self.path_entry = path_entry
        return

    def load_module(self, fullname):
        print('loading %s' % fullname)
        if fullname in sys.modules:
            mod = sys.modules[fullname]
        else:
            mod = sys.modules.setdefault(fullname, imp.new_module(fullname))

        # Set a few properties required by PEP 302
        mod.__file__ = fullname
        mod.__name__ = fullname
        # always looks like a package
        mod.__path__ = [ 'path-entry-goes-here' ]
        mod.__loader__ = self
        mod.__package__ = '.'.join(fullname.split('.')[:-1])

        with open(fullname + '.json') as f:
            mod.__dict__.update(json.load(f))

        return mod


if __name__ == '__main__':
    sys.meta_path.append(JsonImportFinder())
    import sample_config
    from pprint import pprint
    globals().update(sample_config.__dict__)
    print(hello)