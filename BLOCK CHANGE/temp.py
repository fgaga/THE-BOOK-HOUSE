# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
# CREAMOS LA BASE DE DATOS

import pandas as pd
import csv 
import sys# para ejecutar funciones en el sistema
import pathlib #para encontrar la carpeta en la que nos ubicamos
autorColumns = ['Nombre','Info','Ideautor','Foto']
ruta = str(pathlib.Path(__file__).parent.parent.absolute())+'/modelos'
print(ruta)
sys.path.append(ruta)
import Libro 

def crearCsvs():
    
    df = pd.DataFrame([], autorColumns)
    df.to_csv('autor.csv')

    df = pd.DataFrame ([], columns = ['Titulo','Portada','Ideautor','Seccion', 'Pegi', 'Precio', 'Isbn','Editorial'])

    df.to_csv('Libros.csv')
    
# FUNCIONES DE INTRODUCIR EN LA BASE DE DATOS

def crearAutor(autor): # recibimos como parametro el objeto autor
    
    csv.DicWriter(autor.csv,)
    



