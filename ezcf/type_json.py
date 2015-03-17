import os
import json
import sys
from ._base import BaseFinder, BaseLoader, FileFormatError


class JsonFinder(BaseFinder):

    def __init__(self, *args, **kwargs):
        super(JsonFinder, self).__init__(*args, **kwargs)

    def find_module(self, fullname, path=None):

        if '.' in fullname:
            fullname = os.path.join(*([self.dir] + fullname.split('.')))

        if os.path.isfile(fullname + '.json'):
            return JsonLoader(self.dir)
        else:
            return None


class JsonLoader(BaseLoader):

    TYPE = 'json'

    def __init__(self, *args, **kwargs):
        self.e = None
        super(JsonLoader, self).__init__(*args, **kwargs)

    def load_module(self, fullname):
        """
        load_module is always called with the same argument as finder's
        find_module, see "How Import Works"
        """
        mod = super(JsonLoader, self).load_module(fullname)

        if '.' in fullname:
            fullname = os.path.join(*([self.dir] + fullname.split('.')))

        fullname = fullname + '.' + self.TYPE

        try:
            with open(fullname) as f:
                mod.__dict__.update(json.load(f))
        except ValueError:
            # if raise here, traceback will contain ValueError
            self.e = "ValueError"
            self.err_msg = sys.exc_info()[1]

        if self.e == "ValueError":
            err_msg = '\n\t' + self.TYPE + " not valid: "
            err_msg += fullname + '\n'
            err_msg += '\t' + str(self.err_msg)
            raise FileFormatError(err_msg)

        return mod