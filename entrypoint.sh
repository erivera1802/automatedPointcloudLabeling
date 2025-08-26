#!/bin/sh
cd /MS3D
python setup.py develop
cd tracker
pip install -e . --user
cd ..
cd tools/
git config --global --add safe.directory /MS3D
