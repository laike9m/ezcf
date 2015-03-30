import os
import json
import sys
import codecs
from ._base import BaseFinder, BaseLoader, InvalidJsonError


class JsonFinder(BaseFinder):

    def __init__(self, *args, **kwargs):
        self.ext_name = ".json"
        super(JsonFinder, self).__init__(*args, **kwargs)

    def find_module(self, fullname, path=None):

        cfg_file = self.get_cfg_filepath(fullname)

        if os.path.isfile(cfg_file + self.ext_name):
            return JsonLoader(cfg_file + self.ext_name)
        else:
            return None


class JsonLoader(BaseLoader):

    def __init__(self, cfg_file, *args, **kwargs):
        self.e = None
        self.err_msg = None
        self.cfg_file = cfg_file
        super(JsonLoader, self).__init__(*args, **kwargs)

    def load_module(self, fullname):
        """
        load_module is always called with the same argument as finder's
        find_module, see "How Import Works"
        """
        mod = super(JsonLoader, self).load_module(fullname)

        try:
            with codecs.open(self.cfg_file, 'r', 'utf-8') as f:
                mod.__dict__.update(json.load(f))
        except ValueError:
            # if raise here, traceback will contain ValueError
            self.e = "ValueError"
            self.err_msg = sys.exc_info()[1]

        if self.e == "ValueError":
            err_msg = "\nJson not valid: "
            err_msg += self.cfg_file + '\n'
            err_msg += str(self.err_msg)
            raise InvalidJsonError(err_msg)

        return mod