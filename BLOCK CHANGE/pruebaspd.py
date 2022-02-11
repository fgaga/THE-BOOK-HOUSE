#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 13:11:33 2022

@author: fatimagarcia
"""

import pandas as pd
df = pd.read_csv("libros.csv",index_col='Libro'
                 #ESTOS FICHEROS TIENEN QUE COEXISTIR EN EL MISMO CARPETA 
                 )
print (df)


