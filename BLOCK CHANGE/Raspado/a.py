# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 23:46:02 2022

@author: Luis
"""

import scrapy 
import pandas as pd 
import sys 

print(sys.path)
# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess

import pathlib
import sys
modelos=str(pathlib.Path(__file__).parent.parent.absolute())+'\MODELOS'
sys.path.append(modelos)
print(modelos) 

class ScrapyLibros (scrapy.Spider):
    name="casalibro"
    paginas=8 
        
    def start_requests(self): 
        linea=[]
        urls=[]
        with open('rutas.csv','r') as f: 
                for line in f:
                   linea.append(line.split(',')) 
                   print(linea)
                   
        for a in linea :
            
            a[1]="https://www.casadellibro.com/"+a[1]
            urls.append(a[1]) 
        for url in urls :
            yield scrapy.Request(url=url,callback=self.extraer) 

    def extraer (self,response) : 
        titulo=response.xpath('//div[@class="border-left col-md-4 col-12"]//text()') # Sacamos los titulos de los libros .
        autor=response.css('a.author.text-underline-over::text') # Sacamos los autores de los libros .
        sinopsi=response.xpath('//div[@class="short"]/text()')
        titulos=[[t] for t in titulo.extract()] # Limpiamos los libros y los introduciomos en una lista .
        autores =[t.strip() for t in autor.extract()] # Limpiamos los autores y los introduciomos en una lista .
        sinopsiss=[t.strip() for t in sinopsi.extract()] 
        # Guardamos ambos en la lista dic para así poder acceder a ellos posteriormente . (1 y 2)
        dh=[]
        for i in titulos:
         if(i!=''):
           print(i)
           dh.append(i)  
           dc_dict.append(dh)
        print('termina')
        for i in autores:
          dc_dict1.append(i) # 2
          print(i)
        for i in sinopsiss:
          sinopsis.append(i) # 2
          

#Creamos la variable que guardará los datos :

dc_dict =[]
dc_dict1 =[]
sinopsis=[]
#Creamos e iniciamos la futura red que obtendrá los datos 
process = CrawlerProcess()
process.crawl (ScrapyLibros)
process.start() 
 
def analizar (a):
    bol=True
    lista=[]
    for b in a :
        
        if(bol):
            lista.append(b)
            bol=False
        else:bol=True
    return lista
    
dc_dict=analizar(dc_dict)    

print(len(dc_dict))
print(dc_dict1)
print(len(sinopsis))
data = {'Libro':dc_dict[0:117],
        'Autor':dc_dict1[0:117],
        'Sinopsis':sinopsis[0:117]} 

df = pd.DataFrame(data, columns = ['Libro','Autor','Sinopsis'])
df.to_csv('libros.csv')
