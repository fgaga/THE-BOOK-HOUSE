# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import csv

df = pd.DataFrame([], columns = ['Libro','Autor','Sinopsis'])
df.to_csv('libros.csv')


