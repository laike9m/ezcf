ezcf
====

|Build Status| |Supported Python versions| |PyPI version| |Coverage
Status|

ezcf stands for **easy configuration**, it allows you to import
JSON/YAML/INI like .py files. It is useful whenever you need to read
from these formats, especially for reading configuration files.

OK, stop talking, show us some code!

On the left is what you'll normally do, on the right is the ezcf way.
Much more elegant isn't it?

.. figure:: https://github.com/laike9m/ezcf/raw/master/code_compare.png
   :alt: 

Install
-------

::

    pip install ezcf

If you run into ``error: yaml.h: No such file or directory``, don't
worry, you can still use ezcf without any problem.

Supported File Types
--------------------

ezcf supports ``JSON``, ``YAML``, ``INI`` and ``XML`` with extension
``json``, ``yaml``, ``yml``, ``ini``, ``xml``.

Sample Usage
------------

ezcf supports all kinds of valid import statements, here's an example:

::

    ├── subdir
    │   ├── __init__.py
    │   └── sample_yaml.yaml
    ├── test_normal.py
    └── sample_json.json

Various ways to use configurations in ``sample_yaml.yaml`` and
``sample_json.json``:

.. code:: python

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

You can assume they're just regular python files.(Currently ezcf only
supports files with utf-8 encoding)

What about relative import? Yes, ezcf supports relative import, as long
as you use it *correctly*.

Something to note before using ezcf:

1. ezcf is still in developement. If you find any bug, please report it
   in issues;
2. Be careful importing YAML which contains multiple documents: if there
   exists keys with the same name, only one of them will be loaded. So
   it's better not to use multiple documents;
3. All values in ``.ini`` files are kept as it is and loaded as a
   string;
4. Since XML only allows single root, the whole xml will be loaded as
   one dict with root's name as variable name;
5. Namespace package is not supported yet, pull requests are welcome.

Run Tests
---------

::

    python setup.py test

Roadmap
-------

-  [x] Use dot to seperate folder/subfolder/file
-  [x] Unicode support
-  [x] JSON support
-  [x] YAML support
-  [x] INI support
-  [x] XML support
-  [ ] Auto encoding detect?
-  [x] CI
-  [x] coverage
-  [x] pypi

License
-------

MIT

.. |Build Status| image:: https://travis-ci.org/laike9m/ezcf.svg
   :target: https://travis-ci.org/laike9m/ezcf
.. |Supported Python versions| image:: https://pypip.in/py_versions/ezcf/badge.svg
   :target: https://pypi.python.org/pypi/ezcf/
.. |PyPI version| image:: https://badge.fury.io/py/ezcf.svg
   :target: http://badge.fury.io/py/ezcf
.. |Coverage Status| image:: https://coveralls.io/repos/laike9m/ezcf/badge.svg
   :target: https://coveralls.io/r/laike9m/ezcf
