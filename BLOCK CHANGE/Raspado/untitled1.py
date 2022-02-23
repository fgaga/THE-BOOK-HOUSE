
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 11:18:35 2022

@author: fatimagarcia
"""
import json
import pathlib
import sys
modelos=str(pathlib.Path(__file__).parent.parent.parent.absolute())+'/MODELOS'
print(modelos)
sys.path.append(modelos)
from Libro import Libro ,Autor


def cargar():
    score=[]
    with open("file.json", 'r') as f:
        score = json.load(f)
        return score
    
    
    
    
def cargarAutores (matriz):
    autores=[]
    for i in matriz:
        try: 
            aux=Autor(i[0][0],i[0][1])
            try: 
                aux.setInfo(i[0][2])
            except:
                print('sin info : ',i)
            autores.append(aux)
            if(i[1]!=[]):aux.setFoto(i[1]) 

            autores.append(aux)
                
        except:
            print('Datos erroneos : ',i[0]) 
    return (autores)
mat=cargar()
m=cargarAutores(mat)