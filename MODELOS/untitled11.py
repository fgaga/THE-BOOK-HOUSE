#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 13:12:20 2022

@author: fatimagarcia
"""

import mysql.connector as mysql
host= '200.200.200.1'
bd= 'book_house'
usuario='fatima' 
password= '123456789'
conexion= mysql.connect(host=host, database=bd,user=usuario, password=password)
print ('CONEXION',conexion.get_server_info())

"""

CREATE TABLE AUTOR ( Nombre VARCHAR(255),Ideautor int, Foto varchar(100));
CREATE TABLE libro ( Titulo varchar(255), Portada varchar (255), Autor varchar (255),
seccion varchar(100),pegi int, precio int, ISBN varchar (100), Informacion varchar (10000) ,Editorial varchar (100));
CREATE TABLE CLIENTE ( Nombre varchar(255), Direccion varchar (255), Email varchar (255), IdCliente int);



CREATE TABLE COMPRA AS SELECT Idcliente,ISBN FROM libro,CLIENTE;
CREATE TABLE ESCRIBE AS SELECT 	ISBN,Ideautor FROM libro,AUTOR;

 
"""

instruccion= conexion.cursor()
try:
     instruccion.execute("CREATE TABLE AUTOR ( Nombre VARCHAR(255),Ideautor int, Foto varchar(100));")
except: 
     print("ya creada")