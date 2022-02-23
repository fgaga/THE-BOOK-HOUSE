#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 12:54:43 2021

@author: fatimagarcia y luisbravo

"""
import json
class Autor():  
    def __init__(self,nombre,idautor):
        self.nombre = nombre
        self.info = ""
        self.ideautor = idautor
        self.foto = ""
        
    def setInfo(self,info):
        self.info=info
        
    def setFoto(self,newfoto):
        self.foto = newfoto
        
    def toJson(self):
        json=""
        return json
    def mostrarAutor(self):
        print('*'*50)
        print(self.nombre) 
        print('*'*50)
        
class FichaTecnica():
    def __init__(self): 
        self.seccion = ""
        self.pegi = "" 
        self.isbn = ""
        self.editorial = ""
        
class Libro(Autor,FichaTecnica):# en los parentisis tenemos la herencia de estos dos objetos
    def __init__(self,titulo,autor,ft):
        self.titulo = titulo
        self.autor = autor
        self.FichaTecnica=ft
        
    def setPrecio(self,newprecio)   :#creo una funcion set que me cambie el precio del libro automaticamente
     
         self.precio = newprecio


    