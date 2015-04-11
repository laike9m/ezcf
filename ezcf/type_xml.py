import os
import sys
import codecs
from xml.parsers.expat import ExpatError
import xmltodict
from ._base import BaseFinder, BaseLoader, InvalidXmlError


class XmlFinder(BaseFinder):

    def __init__(self, *args, **kwargs):
        self.ext_name = ".xml"
        super(XmlFinder, self).__init__(*args, **kwargs)

    def find_module(self, fullname, path=None):

        cfg_file = self.get_cfg_filepath(fullname)

        if os.path.isfile(cfg_file + self.ext_name):
            return XmlLoader(cfg_file + self.ext_name)
        else:
            return None


class XmlLoader(BaseLoader):

    def __init__(self, cfg_file, *args, **kwargs):
        self.e = None
        self.err_msg = None
        self.cfg_file = cfg_file
        super(XmlLoader, self).__init__(*args, **kwargs)

    def load_module(self, fullname):
        mod = super(XmlLoader, self).load_module(fullname)

        try:
            with codecs.open(self.cfg_file, 'r', 'utf-8') as f:
                ordered_dict = xmltodict.parse(f.read())
                regular_dict = {
                    key: dict(value) for key, value in ordered_dict.items()
                }
                mod.__dict__.update(regular_dict)
        except ExpatError:
            self.e = "ExpatError"
            self.err_msg = sys.exc_info()[1]

        if self.e == "ExpatError":
            err_msg = "\nxml file not valid: "
            err_msg += self.cfg_file + '\n'
            err_msg += str(self.err_msg)
            raise InvalidXmlError(err_msg)

        return mod