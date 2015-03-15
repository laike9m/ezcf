import os
import json
import sys
from ._base import BaseFinder, BaseLoader


class JsonFinder(BaseFinder):

    def __int__(self, *args, **kwargs):
        super(JsonFinder, self).__init__(*args, **kwargs)

    def find_module(self, fullname, path=None):

        if '.' in fullname:
            fullname = os.path.join(*([self.dir] + fullname.split('.')))

        if os.path.isfile(fullname + '.json'):
            return JsonLoader(self.dir)
        else:
            return None


class JsonLoader(BaseLoader):

    def __int__(self, *args, **kwargs):
        super(JsonLoader, self).__init__(*args, **kwargs)

    def load_module(self, fullname):
        """
        load_module is always called with the same argument as finder's
        find_module, see "How Import Works"
        """
        mod = super(JsonLoader, self).load_module(fullname)

        if '.' in fullname:
            fullname = os.path.join(*([self.dir] + fullname.split('.')))

        with open(fullname + '.json') as f:
            mod.__dict__.update(json.load(f))

        return mod