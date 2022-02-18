# -*- coding: utf-8 -*- 
""" 
Created on Sun Jan 16 23:46:02 2022 
 
@author: Luis 
""" 
import urllib.request 
import json
import scrapy   
import pathlib 
import sys 
from scrapy.crawler import CrawlerProcess 
modelos=str(pathlib.Path(__file__).parent.parent.parent.absolute())+'/MODELOS' 
print(modelos)
sys.path.append(modelos) 
from Libro import Libro 
  
 
class ScrapyLibros (scrapy.Spider): 
    name= 'casalibro'
    paginas=1 
    def start_requests(self): 
        base='https://www.casadellibro.com/libros/' 
        secciones=['cocina','historia-local-de-espana','ciencias-humanas/religion','ciencias-politicas-y-sociales/politica','musica'] 
        self.urls=[base+a+'/' for a in secciones] 
        for url in self.urls : 
            yield scrapy.Request(url=url,callback=self.aux)  
              
 
    def aux(self,response):  
        total_urls=[] 
        for p in self.urls :
            for n in range(self.paginas) : 
                total_urls.append(p+'/p'+str(n))  
            
        for url in total_urls :  
            yield  response.follow(url=url,callback =self.extraer) 
 
           
    def extraer (self,response) :   
        etexto=response.xpath('//div[@class="row align-end"]//@href')  
        texto=[t.strip() for t in etexto.extract()]   
        # Guardamos ambos en la lista dic para así poder acceder a ellos posteriormente . (1 y 2)  
        for i in set(texto):  
            yield  response.follow(url=i,callback =self.extraer1)  
 
 
    def extraer1 (self,response) :   
              """       Sacamos la informacion de pgina por pagina         """ 
              
              autorpag=response.xpath('//a[@class="text--lighten-1 d-flex secondary--text"]//@href')        
              if(autorpag==[]):
                  self.sacarAutor(response) 
              else:
                  self.sacarLibro(response)
               
             
    def sacarAutor(self,response):
        autora=[t for t in response.xpath('//div[@class="col-lg-8 col-12"]//text()').extract()] 
        portada=[t for t in response.xpath('//img[@class="cdl-img active"]//@data-src').extract() ]  
        autores.append([self.comprobar(autora),self.comprobar(portada)])  
    def sacarLibro(self,response):
        info=response.xpath('//div[@class="border-left col-md-4 col-12"]//text()') # Sacamos los titulos de los libros .  
        titulo=response.xpath('//h1[@class="text-h4 mb-2"]//text()') # Sacamos los titulos de los libros .  
        autor=response.xpath('//a[@class="text--lighten-1 d-flex secondary--text"]//text()') # Sacamos los autores de los libros . 
        sinopsis=response.xpath('//div[@class="col-md-8 col-12"]//text()') 
        
        total=[[t for t in info.extract()],[t for t in titulo.extract()],[t for t in autor.extract()] ]   
        total=[self.comprobar(t) for t in total] 
        total.append(self.comprobar([t.strip() for t in sinopsis.extract()]))  
        portada=response.xpath('//div[@class="v-card v-card--flat v-sheet theme--light rounded-0"]//@data-src') 
        total.append(self.comprobar([t.strip() for t in portada.extract()])) 
        try:
                libros.index(total)
           
            
        except:
                libros.append(total) 
          
        
    def comprobar(self,elem): 
              elem=[t.strip() for t in elem]
              aux=[] 
              for i in elem :
                  try:
                          aux.index(i)
                     
                      
                  except:
                          if(i!='' and i!=' ' and i!=',' ):aux.append(i.strip()) 
                   
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




#Reto implementar estas funciones con tk para elegir donde guardar o el archivo que leer?

def guardar (score):   
    with open("file.json", 'w') as f:
        # indent=2 is not needed but makes the file human-readable
        json.dump(score, f, indent=2) 
def cargar(score):
    with open("file.json", 'r') as f:
        score = json.load(f)
        return score
    
""" 
i=0 
for a in autores:  
     
 try: 
    print('*'*50)
    print(a) 
    print('*'*50)
    urllib.request.urlretrieve(a[len(a)-1], "Fotos\local-"+str(i)+".jpg") 
    i+=1 
 except: 
     print('*'*50)
     print(a) 
     print('*'*50)
     
for a in libros:  
     
 try: 
    print('*'*50)
    print(a) 
    print('*'*50)
    urllib.request.urlretrieve(a[len(a)-1], "Fotos\local-"+str(i)+".jpg") 
    i+=1 
 except: 
     print('*'*50)
     print(a) 
     print('*'*50) 
     

"""