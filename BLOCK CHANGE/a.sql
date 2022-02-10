CREATE TABLE Personas (
    PersonaID int,
    Apellido varchar(255),
    Nombre varchar(255),
    Direccion varchar(255),
    Ciudad varchar(255) 
);

CREATE TABLE TablaPrueba AS
SELECT PersonaID, Nombre
FROM Personas;