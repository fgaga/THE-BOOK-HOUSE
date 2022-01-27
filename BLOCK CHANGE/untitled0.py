# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 16:10:25 2022

@author: Luis
"""

import pathlib
import sys
modelos=str(pathlib.Path(__file__).parent.parent.absolute())+'\MODELOS'
sys.path.append(modelos)
print(modelos)
from Libro import *

a=Autor()
