import os
import sys
import codecs
import yaml

from ._base import BaseFinder, BaseLoader, InvalidYamlError


class YamlFinder(BaseFinder):

    def __init__(self, *args, **kwargs):
        super(YamlFinder, self).__init__(*args, **kwargs)

    def find_module(self, fullname, path=None):

        cfg_file = self.get_cfg_filepath(fullname)

        if os.path.isfile(cfg_file + '.yaml'):
            return YamlLoader(cfg_file + '.yaml')
        elif os.path.isfile(cfg_file + '.yml'):
            return YamlLoader(cfg_file + '.yml')
        else:
            return None


class YamlLoader(BaseLoader):

    def __init__(self, cfg_file, *args, **kwargs):
        self.e = None
        self.err_msg = None
        self.cfg_file = cfg_file
        super(YamlLoader, self).__init__(*args, **kwargs)

    def load_module(self, fullname):
        """
        load_module is always called with the same argument as finder's
        find_module, see "How Import Works"
        """
        mod = super(YamlLoader, self).load_module(fullname)

        with codecs.open(self.cfg_file, 'r', 'utf-8') as f:
            try:
                for doc in yaml.load_all(f, yaml.Loader):
                    if isinstance(doc, dict):
                        mod.__dict__.update(doc)
            except yaml.YAMLError:
                self.e = "YAMLError"
                self.err_msg = sys.exc_info()[1]

        if self.e == "YAMLError":
            err_msg = "\nYaml not valid: "
            err_msg += self.cfg_file + '\n'
            err_msg += str(self.err_msg)
            raise InvalidYamlError(err_msg)

        return mod

