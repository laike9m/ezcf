# ezcf

[![Build Status](https://travis-ci.org/laike9m/ezcf.svg)](https://travis-ci.org/laike9m/ezcf)
[![Supported Python versions](https://pypip.in/py_versions/ezcf/badge.svg)](https://pypi.python.org/pypi/ezcf/)
[![PyPI version](https://badge.fury.io/py/ezcf.svg)](http://badge.fury.io/py/ezcf)
[![Coverage Status](https://coveralls.io/repos/laike9m/ezcf/badge.svg)](https://coveralls.io/r/laike9m/ezcf)

ezcf stands for **easy configuration**, it allows you to import JSON/YAML/INI/XML
like .py files. It is useful whenever you need to read from these formats,
especially for reading configuration files.

OK, stop talking, show us some code!  

On the left is what you'll normally do, on the right is the ezcf way.  
**All you need is `import ezcf` first, then `import filename` without extension.** Nothing else!

![](https://github.com/laike9m/ezcf/raw/master/code_compare.png)

For instance, here we want to load file `config.json`. With a single line of code `from config import *`,
everything is done and you're happy.

## Install

    pip install ezcf
    
If you run into `error: yaml.h: No such file or directory`, don't worry,
you can still use ezcf without any problem.

## Supported File Types
ezcf supports `JSON`, `YAML`, `INI` and `XML` with extension `json`, `yaml`, `yml`, `ini`, `xml`.

## Sample Usage
ezcf supports all kinds of valid import statements, here's an example:
```
├── subdir
│   ├── __init__.py
│   └── sample_yaml.yaml
├── test_normal.py
└── sample_json.json
```

Various ways to use configurations in `sample_yaml.yaml` and `sample_json.json`:
```python
import ezcf

from subdir.sample_yaml import *
# or
from subdir.sample_yaml import something
# or
import subdir.sample_yaml as sy
print(sy.something)

from sample_json import *
# or
from sample_json import something
# or
import sample_json as sj
print(sj.something)
```
You can assume they're just regular python files.(Currently ezcf only supports files with utf-8 encoding)

What about relative import? Yes, ezcf supports relative import, as long as you use it *correctly*.

Something to note before using ezcf:

1. ezcf is still in developement. If you find any bug, please report
it in issues;
2. Be careful importing YAML which contains multiple documents: if there exists keys with the same name,
only one of them will be loaded. So it's better not to use multiple documents;
3. All values in `.ini` files are kept as it is and loaded as a string;
4. Since XML only allows single root, the whole xml will be loaded as one dict with root's name as variable name;
5. Namespace package is not supported yet, pull requests are welcome.
6. Use [**valid variable names**][1], this means key strings in JSON/YAML/INI/XML should be valid Python variable name.
 Invalid variable name won't do any harm to your program nor will it crash, but you can't use them as expected.

## Run Tests
```
python setup.py test
```

## Roadmap

- [x] Use dot to seperate folder/subfolder/file
- [x] Unicode support
- [x] JSON support
- [x] YAML support
- [x] INI support
- [x] XML support
- [ ] Auto encoding detect?
- [x] CI
- [x] coverage
- [x] pypi

## License
MIT


[1]: https://docs.python.org/3.4/reference/lexical_analysis.html#identifiers