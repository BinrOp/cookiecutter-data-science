#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    interface with personal Library

"""
import sys
import os
file_path = os.path.realpath(__file__)
print file_path

# local
import cnf
import paths

# global
scripts_path = os.path.realpath(file_path+'/../../../')+ "/tools"
sys.path.append(scripts_path)
