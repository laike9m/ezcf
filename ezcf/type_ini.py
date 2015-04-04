import os
import sys
from configobj import ConfigObj
from ._base import BaseFinder, BaseLoader, InvalidIniError


class IniFinder(BaseFinder):

    def __init__(self, *args, **kwargs):
        self.ext_name = ".ini"
        super(IniFinder, self).__init__(*args, **kwargs)

    def find_module(self, fullname, path=None):

        cfg_file = self.get_cfg_filepath(fullname)

        if os.path.isfile(cfg_file + self.ext_name):
            return IniLoader(cfg_file + self.ext_name)
        else:
            return None


class IniLoader(BaseLoader):

    def __init__(self, cfg_file, *args, **kwargs):
        self.e = None
        self.err_msg = None
        self.cfg_file = cfg_file
        super(IniLoader, self).__init__(*args, **kwargs)

    def load_module(self, fullname):
        mod = super(IniLoader, self).load_module(fullname)

        try:
            config = ConfigObj(self.cfg_file, encoding='UTF8',
                               raise_errors=True)
            mod.__dict__.update(dict((k, config[k]) for k in config.keys()))
        except SyntaxError:
            self.e = "IniError"
            self.err_msg = sys.exc_info()[1]

        if self.e == "IniError":
            err_msg = "\nIni file not valid: "
            err_msg += self.cfg_file + '\n'
            err_msg += str(self.err_msg)
            raise InvalidIniError(err_msg)

        return mod