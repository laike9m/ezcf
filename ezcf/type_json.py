import os
import json
import sys
import codecs
from ._base import BaseFinder, BaseLoader, InvalidJsonError


class JsonFinder(BaseFinder):

    def __init__(self, *args, **kwargs):
        super(JsonFinder, self).__init__(*args, **kwargs)

    def find_module(self, fullname, path=None):

        cfg_file, caller_file_dir = self.get_cfg_filepath(fullname)

        if os.path.isfile(cfg_file + '.json'):
            return JsonLoader(caller_file_dir)
        else:
            return None


class JsonLoader(BaseLoader):

    TYPE = 'json'

    def __init__(self, dir):
        self.e = None
        self.err_msg = None
        super(JsonLoader, self).__init__(dir)

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
            with codecs.open(fullname, 'r', 'utf-8') as f:
                mod.__dict__.update(json.load(f))
        except ValueError:
            # if raise here, traceback will contain ValueError
            self.e = "ValueError"
            self.err_msg = sys.exc_info()[1]

        if self.e == "ValueError":
            err_msg = '\n' + self.TYPE + " not valid: "
            err_msg += fullname + '\n'
            err_msg += str(self.err_msg)
            raise InvalidJsonError(err_msg)

        return mod