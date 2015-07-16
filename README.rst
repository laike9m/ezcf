ezcf
====

|Build Status| |Supported Python versions| |PyPI version| |Coverage
Status|

ezcf stands for **easy configuration**, it allows you to import
JSON/YAML/INI/XML like .py files. It is useful whenever you need to read
from these formats, especially for reading configuration files.

OK, stop talking, show us some code!

| On the left is what you'll normally do, on the right is the ezcf way.
| **All you need is ``import ezcf`` first, then ``import filename``
  without extension.** Nothing else!

.. figure:: https://github.com/laike9m/ezcf/raw/master/code_compare.png
   :alt: 

For instance, here we want to load file ``config.json``. With a single
line of code ``from config import *``, everything is done and you're
happy.

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

Let's start with an easy case:

::

    ├── sample1.py
    └── sample1.json  

``sample1.py`` and ``sample1.json`` are in the same directory. We want
to read ``sample1.json`` in ``sample1.py``, here's how:

.. code:: python

    """
    # sample1.json
    {
        "hello": "world"
    }
    """

    # sample1.py
    import ezcf
    from sample1 import hello

    print(hello)  # 'world'

It's that easy.

 That's cool, but we usually put config files in a separate folder. Can
ezcf deal with that?

::

    ├── conf
    │   ├── __init__.py
    │   └── sample2.yaml
    └── sample2.py

Why not?

.. code:: python

    """sample2.yaml
    ---
    Time: 2001-11-23 15:02:31 -5
    User: ed
    warning:
      This is a warning.
    ---
    Date: 2001-11-23 15:03:17 -5
    User: ed
    Fatal:
      Unknown variable "bar"
    Stack:
      - file: TopClass.py
        line: 23
        code: |
          x = MoreObject("345\n")
      - file: MoreClass.py
        line: 58
        code: |-
          foo = bar
    """

    # sample2.py
    import ezcf
    from conf.sample2 import Time, User, warning, Stack

    Time  # datetime.datetime(2001, 11, 23, 20, 2, 31)
    User  # ed
    warning  # This is a warning.
    Stack  # [{'line': 23, 'code': 'x = MoreObject("345\\n")\n', 'file': 'TopClass.py'}, {'line': 58, 'code': 'foo = bar', 'file': 'MoreClass.py'}]

ezcf supports all kinds of valid import statements. These statements are
equivalent:

.. code:: python

    from conf.sample2 import Time, User, warning, Stack
    from conf.sample2 import *
    import conf.sample2  # then use conf.sample2.Time/User/warning/Stack
    import conf.sample2 as cs  # then use cs.Time/User/warning/Stack

In a word, you can assume they're just regular python files.(Currently
ezcf only supports files with utf-8 encoding)

What about relative import? Yes, ezcf supports relative import, as long
as you use it *correctly*.

Note
----

1. Be careful importing YAML which contains multiple documents: if there
   exists keys with the same name, only one of them will be loaded. So
   it's better not to use multiple documents;
2. All values in ``.ini`` files are kept as it is and loaded as a
   string;
3. Since XML only allows single root, the whole xml will be loaded as
   one dict with root's name as variable name;
4. Use `**valid variable
   names** <https://docs.python.org/3.4/reference/lexical_analysis.html#identifiers>`__,
   this means key strings in JSON/YAML/INI/XML should be valid Python
   variable name. Invalid variable name won't do any harm to your
   program nor will it crash, but you can't use them as expected.

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
.. |Supported Python versions| image:: https://img.shields.io/pypi/pyversions/ezcf.svg
   :target: https://pypi.python.org/pypi/ezcf/
.. |PyPI version| image:: https://badge.fury.io/py/ezcf.svg
   :target: http://badge.fury.io/py/ezcf
.. |Coverage Status| image:: https://coveralls.io/repos/laike9m/ezcf/badge.svg
   :target: https://coveralls.io/r/laike9m/ezcf
