#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 13:12:20 2022

@author: fatimagarcia
"""

import mysql.connector as mysql
host= '127.0.0.128'
bd= ''
usuario='fatima'
password= '123456789'
conexion= mysql.connect(host=host, database=bd,user=usuario, password=password)
print ('CONEXION',conexion.get_server_info())

