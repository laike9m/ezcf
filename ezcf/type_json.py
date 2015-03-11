import os
import json
from ._base import BaseFinder, BaseLoader


class JsonFinder(BaseFinder):

    def __int__(self, *args, **kwargs):
        super(JsonFinder, self).__init__(*args, **kwargs)

    def find_module(self, fullname, path=None):
        print('JsonImportFinder looking for "%s" with path "%s"' %
              (fullname, path))
        if os.path.isfile(fullname + '.json'):
            return JsonLoader(fullname + '.json')
        else:
            return None


class JsonLoader(BaseLoader):

    def __int__(self, *args, **kwargs):
        super(JsonLoader, self).__init__(*args, **kwargs)

    def load_module(self, fullname):
        mod = super(JsonLoader, self).load_module(fullname)

        with open(fullname + '.json') as f:
            mod.__dict__.update(json.load(f))

        return mod