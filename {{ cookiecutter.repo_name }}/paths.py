#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
file_path = os.path.realpath(__file__)
print file_path

# environment variables
PROJECT = os.path.dirname(file_path) + '/'

DATA = os.path.realpath(file_path+'/../../../')+ "/data/"
PRODUCTS = os.path.realpath(file_path+'/../../../')+ "/products/"

MODELS = PROJECT+ 'data/models/'
DEPS = PROJECT+ 'data/deps/'
PROCESSED= PROJECT+ 'data/processed/'
INTERIM= PROJECT+ 'data/interim/'
TEST = PROJECT+ 'data/test/'
GEN_NB= PROJECT+ 'notebooks/gen/'
GEN = PROJECT+ 'data/gen/'
REPORTS = PROJECT + 'reports/'
