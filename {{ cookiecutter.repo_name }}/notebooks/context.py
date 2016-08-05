#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

project_path = os.path.realpath('../')
print project_path

sys.path.append(project_path)

from env import *

# specific to notebooks !
from tools.nb.init_nb_env import *
