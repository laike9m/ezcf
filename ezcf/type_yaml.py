import os
import sys
import yaml

from ._base import BaseFinder, BaseLoader


class YamlFinder(BaseFinder):

    def __int__(self, *args, **kwargs):
        super(YamlFinder, self).__init__(*args, **kwargs)

    def find_module(self, fullname, path=None):

        if '.' in fullname:
            fullname = os.path.join(*([self.dir] + fullname.split('.')))

        if os.path.isfile(fullname + '.yaml'):
            return YamlLoader(self.dir)
        else:
            return None


class YamlLoader(BaseLoader):

    def __int__(self, *args, **kwargs):
        super(YamlLoader, self).__init__(*args, **kwargs)

    def load_module(self, fullname):
        """
        load_module is always called with the same argument as finder's
        find_module, see "How Import Works"
        """
        mod = super(YamlLoader, self).load_module(fullname)

        if '.' in fullname:
            fullname = os.path.join(*([self.dir] + fullname.split('.')))

        with open(fullname + '.yaml') as f:
            for doc in yaml.load_all(f, yaml.Loader):
                mod.__dict__.update(doc)

        return mod

