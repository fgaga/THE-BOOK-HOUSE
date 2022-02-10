# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 23:46:02 2022

@author: Luis
"""
import urllib.request

import scrapy  
import pathlib
import sys
from scrapy.crawler import CrawlerProcess
modelos=str(pathlib.Path(__file__).parent.parent.parent.absolute())+'\\MODELOS'
sys.path.append(modelos)
from libro import Libro  
 

class ScrapyLibros (scrapy.Spider): 
    paginas=12
   
    def start_requests(self):
        base='https://www.casadellibro.com/libros/'
        secciones=['cocina','historia-local-de-espana','ciencias-humanas/religion','ciencias-politicas-y-sociales/politica','musica']
        urls=[base+a+'/' for a in secciones]
        for url in urls :
            yield scrapy.Request(url=url,callback=self.aux) 
             

    def aux(self,response): 
        urls=[]
        for n in range(self.paginas) :
            urls.append(response.url+'/p'+str(n)) 

        for url in urls : 
            yield  response.follow(url=url,callback =self.extraer)

          
    def extraer (self,response) :  
        etexto=response.xpath('//div[@class="row align-end"]//@href') 
        texto=[t.strip() for t in etexto.extract()] 
        # Guardamos ambos en la lista dic para así poder acceder a ellos posteriormente . (1 y 2) 
        for i in texto: 
            yield  response.follow(url=i,callback =self.extraer1) 


    def extraer1 (self,response) :  
              """       Sacamos la informacion de pgina por pagina         """
              
              info=response.xpath('//div[@class="border-left col-md-4 col-12"]//text()') # Sacamos los titulos de los libros . 
              titulo=response.xpath('//h1[@class="text-h4 mb-2"]//text()') # Sacamos los titulos de los libros . 
              autor=response.xpath('//a[@class="text--lighten-1 d-flex secondary--text"]//text()') # Sacamos los autores de los libros .
              sinopsi=response.xpath('//div[@class="short"]//text()')
              
              total=[[t for t in info.extract()],[t for t in titulo.extract()],[t for t in autor.extract()] ]  
              total=[self.comprobar(t) for t in total]
              total.append(self.comprobar([t.strip() for t in sinopsi.extract()]))
              
              if(total[0]==[]): 
                  autora=response.xpath('//div[@class="col-lg-8 order-lg-1 col-12"]//text()')
                  portada=response.xpath('//div[@class="col-lg-4 col-auto"]//@data-src') 
                  portada=[t.strip() for t in portada.extract()]  
                  autorz=[t.strip() for t in autora.extract()]
                  autores.append(self.comprobar(autorz))
                  autores.append(portada)
              else:
                  portada=response.xpath('//div[@class="v-card v-card--flat v-sheet theme--light rounded-0"]//@data-src')
                  portada=[t.strip() for t in portada.extract()] 
              
      
  
                  libros.append(total)
                  libros.append(portada)
              
    def comprobar(self,elem):
              aux=[]
              for i in elem:
                  if(i!='' and i!=' ' and i!=','):aux.append(i.replace('\n',""))
                  
              return aux
           

# the wrapper to make it run more times 
libros=[]
autores=[]

#Creamos la variable que guardará los datos :
  
datos=[]
bookid=[]
#Creamos e iniciamos la futura red que obtendrá los datos

process = CrawlerProcess()
process.crawl (ScrapyLibros)
process.start()

i=0
for a in autores: 
    
 try:
    print(a)
    urllib.request.urlretrieve(a[len(a)-1], "Fotos\local-"+str(i)+".jpg")
    i+=1
 except:
     print('*'*50)
for a in libros: 
 try:
    print(a)
    urllib.request.urlretrieve(a[len(a)-1], "Fotos\local-"+str(i)+".jpg")
    i+=1
 except:
     print('*'*50)
 
      