import scrapy 
import pandas as pd 
import sys 

print(sys.path)
# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess



#   --------------------------------------------------------------------------------------------------

#   Este tipo de importacion lo que hace es guardar en el sistema la carpeta 
#   de los modelos para posteriormente importar cualquier archivo que se encuentre en
#   el array de caminos del sistema.
#
#

import pathlib # Nos sirve para encontrar la carpeta principal 


# Cuando el codigo es ejecutado el systema tiene por defecto algunos caminos predefinidos , si ejecutamos la siguiente instrucccion :
import csv

#Lo que esta haciendo el sistema es encontrar un archivo llamado csv en un conjunto (sys.path) de rutas (carpetas) , basicamente comprueba que
#exista un archivo csv en alguna carpeta.

import sys 
""" Este módulo provee acceso a algunas variables usadas o mantenidas por el intérprete 
    =>Nos permite cargar de forma muy sencilla archivos de un proyecto """
    
    
    #pathlib.Path(__file__) Nos permite obtener la ruta del archivo ejecutado
    #.parent nos permie retroceder un elemento
    #.absolute() Nos la la ruta mas corta hacia una carpeta u archivo
    
modelos= str(pathlib.Path(__file__).parent.parent.absolute()) #Tiene str por que para cargar una ruta en el sistema necesitamos
#que sea texto para poder modelarla a nuestro antojo

modelos+='\MODELOS'#Queremos cargar los archivos de esta carpeta para asi en el raspado darles forma.
sys.path.append(modelos)#metemos la ruta en el conjunto de rutas del hilo.



#   --------------------------------------------------------------------------------------------------
 

class ScrapyLibros (scrapy.Spider):
    name="casalibro"
    paginas=8
    def start_requests(self):
        urls=['https://www.casadellibro.com/libros/cocina/106000000']
        for url in urls :
            yield scrapy.Request(url=url,callback=self.aux)

    def aux(self,response):
        urls=[]
        for n in range(self.paginas) :
            urls.append('https://www.casadellibro.com/libros/cocina/106000000/p'+str(n)) 

        for url in urls : 
           yield  response.follow(url=url,callback =self.extraer)

    def extraer (self,response) :  
        etexto=response.xpath('//div[@class="row align-end"]//@href') 
        texto=[t.strip() for t in etexto.extract()] 
        # Guardamos ambos en la lista dic para así poder acceder a ellos posteriormente . (1 y 2) 
        for i in texto:
          datos.append(i) 

#Creamos la variable que guardará los datos :
 
datos=[]
bookid=[]
#Creamos e iniciamos la futura red que obtendrá los datos

process = CrawlerProcess()
process.crawl (ScrapyLibros)
process.start()

 
 
for i in datos :
    i='https://www.casadellibro.com'+str(i) 
    print(i)
    
data = {'Libro':datos
        } 

df = pd.DataFrame(data, columns = ['Libro' ])
df.to_csv('rutas.csv')