#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 12:54:43 2021

@author: fatimagarcia y luisbravo

"""

Libro.Autor()
Libro.Libro()
class Autor():  
    def __init__(self,nombre,info,ideautor,foto):
        self.nombre = nombre
        self.info = info
        self.ideautor = ideautor
        self.foto = foto
        
    def setFoto(self,newfoto):
        self.foto = newfoto
    
class Libro(Autor):# en los parentisis tenemos la herencia de estos dos objetos
    def __init__(self,titulo,portada,autor,seccion,pegi,precio,isbn,editorial):
        self.titulo = titulo
        self.portada = portada
        self.autor = autor
        self.seccion = seccion
        self.pegi = pegi
        self.precio = precio
        self.isbn = isbn
        self.editorial = editorial
        
    def setPrecio(self,newprecio)   :#creo una funcion set que me cambie el precio del libro automaticamente
     
         self.precio = newprecio
         
         

    