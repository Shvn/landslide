#!/usr/bin/env bash

python landslide/runserver.py > /dev/null &
nosetests --with-coverage