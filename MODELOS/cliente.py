#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 13:36:12 2022

@author: fatimagarcia
"""

class Cliente():
    def __init__(self,nombre,email,idencliente,direccion):
        self.nombre = nombre
        self. email = email
        self. idencliente = idencliente
        self. direccion = direccion
        
    def setNewdireccion(self,Newdireccion):
        self.direccion= Newdireccion
        