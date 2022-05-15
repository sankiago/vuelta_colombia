import sqlite3
from sqlite3 import Error

def conexionALaBD():
    try:
        con=sqlite3.connect('BDEjemplo.db')
        return con
    except Error:
        print(Error)

class Estudiante:
    def __init__(self):
        self.cedula=None
        self.nombre=None
        self.apellido=None
        self.etapa=None
        self.tiempo=None

    def crearTabla(self,con):
        cursorObj=con.cursor()
        cursorObj.execute("CREATE TABLE estudiante (cedula integer, nombre text, apellido text, etapa integer, tiempo integer)")
        con.commit()

    def leerinfo(self):
        self.cedula=input("Cedula: ")
        self.cedula=self.cedula.ljust(12)
        self.nombre=input("Nombre: ")
        self.apellido=input("Apellido: ")
        self.etapa=input("Etapa: ")
        self.tiempo=input("Tiempo: ")
        self.estudiante=(self.cedula,self.nombre,self.apellido,self.etapa,self.tiempo)
        return self.estudiante

    def insertarTabla(self,con,estudiante):
        cursorObj=con.cursor()
        #cursorObj.execute("INSERT INTO estudiante VALUES (1234567891,'Tatiana','Barrios')")
        cursorObj.execute('''INSERT INTO estudiante VALUES(?,?,?,?,?)''',estudiante)
        con.commit()

    def actualizarTabla(self,con):
        cursorObj=con.cursor()
        nombre=input("Nombre: ")
        self.actualizar='UPDATE estudiante SET nombre ="'+nombre+'" WHERE cedula=1'
        print("La cadena que se ejecutará es: ",self.actualizar)
        cursorObj.execute(self.actualizar)
        con.commit()
    def insertarTabla(self,con,estudiante):
        cursorObj=con.cursor()
        #cursorObj.execute("INSERT INTO estudiante VALUES (1234567891,'Tatiana','Barrios')")
        cursorObj.execute('''INSERT INTO estudiante VALUES(?,?,?,?,?)''',estudiante)
        con.commit()
    def actualizarTabla(self,con):
        cursorObj=con.cursor()
        self.nombre=input("Nombre: ")
        self.actualizar='UPDATE estudiante SET nombre ="'+self.nombre+'" WHERE cedula=1'
        print("La cadena que se ejecutará es: ",self.actualizar)
        cursorObj.execute(self.actualizar)
        con.commit()
    def consultaTabla(self,con):
        cursorObj=con.cursor()
        #consulta="SELECT cedula, nombre FROM estudiante"
        self.consulta="SELECT * FROM estudiante"
        cursorObj.execute(self.consulta)
        filas=cursorObj.fetchall()
        for row in filas:
            cedula=row[0]
            nombre=row[1]
            print ("La información de la tupla es: ")
            print(row)
            print ("El estudiante es: ",cedula," ",nombre)
    def borrarRegistroTabla(self,con):
        cursorObj=con.cursor()
        cursorObj.execute("DELETE FROM estudiante WHERE cedula=123")
        con.commit()
    def consultaClasificacionGeneral(self,con):
        cursorObj=con.cursor()
        self.consulta="SELECT cedula, nombre, apellido, sum(tiempo) FROM estudiante group by cedula"
        cursorObj.execute(self.consulta)
        filas=cursorObj.fetchall()
        for row in filas:
            #cedula=row[0]
            #nombre=row[1]
            print ("La información de la tupla es: ")
            print(row)
            #print ("El estudiante es: ",cedula," ",nombre)

miCon=conexionALaBD()
Tania=Estudiante()
Joel=Tania.consultaTabla(miCon)
