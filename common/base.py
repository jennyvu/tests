#!/usr/bin/env python
import os
import sys

def get_base_dir():
    home_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    return home_dir
