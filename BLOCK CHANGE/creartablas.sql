

CREATE TABLE AUTOR ( Nombre VARCHAR(255),Ideautor int, Foto varchar(100));
CREATE TABLE libro ( Titulo varchar(255), Portada varchar (255), Autor varchar (255),
seccion varchar(100),pegi int, precio int, ISBN varchar (100), Informacion varchar (10000) ,Editorial varchar (100));
CREATE TABLE CLIENTE ( Nombre varchar(255), Direccion varchar (255), Email varchar (255), IdCliente int);



CREATE TABLE COMPRA AS SELECT Idcliente,ISBN FROM libro,CLIENTE;
CREATE TABLE ESCRIBE AS SELECT 	ISBN,Ideautor FROM libro,AUTOR;

 
