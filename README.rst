ezcf
====

|Build Status|

ezcf stands for **easy configuration**, it allows you to import
JSON/YAML like importing .py files, which is very useful for reading
conf files with these formats.

Install
-------

::

    pip install ezcf

Note: if you run into ``error: yaml.h: No such file or directory``,
don't worry, you can still use ezcf without any problem.

Sample Usage
------------

::

    ├── subdir
    │   ├── __init__.py
    │   └── sample_yaml.yaml
    ├── test_normal.py
    └── sample_json.json

If you want to use configurations in ``sample_yaml.yaml`` and
``sample_json.json``, here's how:

.. code:: python

    import ezcf
    from subdir.sample_yaml import *
    from sample_json import something

You can assume they're regular python files.(Currently ezcf only
supports files with utf-8 encoding)

``ezcf`` is still in developement, use it at your own risk. If you find
any bug, please report it in issues.

Roadmap
-------

-  [x] Use dot to seperate folder/subfolder/file
-  [x] Unicode support
-  [x] JSON support
-  [x] YAML support
-  [ ] INI support
-  [ ] Auto encoding detect?
-  [x] CI
-  [ ] coverage
-  [x] pypi

.. |Build Status| image:: https://travis-ci.org/laike9m/ezcf.svg
   :target: https://travis-ci.org/laike9m/ezcf
