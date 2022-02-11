#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 13:16:10 2022

@author: fatimagarcia
"""
#esto es un ejemplo en mongodb 
import pymongo 
token= 'mongodb+srv://fgaga:<1234567890>@cluster0.iiqes.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
dbUrl=pymongo.MongoClient(token)
db = dbUrl['pytondb']#nombre de la base de datos
collection= db ['user']#nombre dela coleccion

db.collection.insert_many([{'name':'keyboard','price':300,'tienda':'mediamark'}])
    
#inserto registro
        
        