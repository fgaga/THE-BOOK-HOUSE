# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import csv

df = pd.DataFrame([], columns = ['Nombre','Info','Ideautor','Foto'])
df.to_csv('autor.csv')

df = pd.DataFrame ([], columns = ['Titulo','Portada','Ideautor','Seccion', 'Pegi', 'Precio', 'Isbn','Editorial'])

df.to_csv('Libros.csv')

