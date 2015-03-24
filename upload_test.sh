#!/usr/bin/env bash
python setup.py register -r test
python setup.py sdist upload -r test
python setup.py bdist_wheel upload -r test