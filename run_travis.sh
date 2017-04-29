#!/usr/bin/env bash
python runserver.py > /dev/null &
nosetests --with-coverage