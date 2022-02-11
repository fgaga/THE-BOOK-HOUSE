#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 12:56:20 2022

@author: fatimagarcia
"""
import pathlib
import sys
modelos=str(pathlib.Path(__file__).parent.absolute())+'\MODELOS'
sys.path.append(modelos)
import Libro.Autor as Autor
import csv 
libros=[]
autor=[]
with open ('libros.csv')as libro:
    reader_obj = csv.reader(libro)
    for row in reader_obj:
        c=Autor(row[2],row[0],"")
        autor.append(c)
        
        
        
print(autor)