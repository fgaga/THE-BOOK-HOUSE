#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 12:54:43 2021

@author: fatimagarcia y luisbravo

"""
 
class Autor():  
    def __init__(self,nombre,ideautor,foto):
        self.nombre = nombre
    
        self.ideautor = ideautor
        self.foto = foto
        
    def setFoto(self,newfoto):
        self.foto = newfoto
    def mostrarAutor(self):
        print(50*'-')
        print('nombre del autor',self.nombre)
        print(50*'-')
    
class Libro(Autor):# en los parentisis tenemos la herencia de estos dos objetos
    def __init__(self,titulo,sinopsis,autor,seccion,pegi,precio,isbn,editorial):
        self.titulo = titulo
        
        self.autor = autor
        self.seccion = seccion
        self.pegi = pegi
        self.precio = precio
        self.isbn = isbn
        self.editorial = editorial
        self.sinopsis=sinopsis
    def mostrarLibro (self):
        print(50*'-')
        print ('nombre del libro',self.titulo )
        print ('sinopsis',self.sinopsis)
        print(50*'-')
        
    def setPrecio(self,newprecio)   :#creo una funcion set que me cambie el precio del libro automaticamente
     
         self.precio = newprecio
         
         
         

    