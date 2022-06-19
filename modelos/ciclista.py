#Modelos 
#ciclista.py
import re
from modelos.modelo import Modelo

class Ciclista(Modelo):
  def __init__(self, lista_de_informacion=None, num_identificacion=None, nombre=None, apellido=None, fotografia=None, fecha_nacimiento=None, pais=None, num_equipo=None, ranking_UCI=None):
    if lista_de_informacion != None:
        self.num_inscripcion, self.num_identificacion, self.nombre, self.apellido, self.fotografia, self.fecha_nacimiento_formateada, self.pais, self.num_equipo, self.ranking_UCI = lista_de_informacion
    else:
        self.num_identificacion = num_identificacion
        self.nombre             = nombre
        self.apellido           = apellido
        self.fotografia         = fotografia
        self.fecha_nacimiento   = fecha_nacimiento
        self.pais               = pais
        self.num_equipo         = num_equipo
        self.ranking_UCI         = ranking_UCI
        #sin implementar: fotografia = input('Fotografía: ')

        dia, mes, anio = fecha_nacimiento.split('/')
        if len(fecha_nacimiento.split('/')) != 3 or (len(dia) != 2 or len(mes) != 2 or len(anio) != 4):
            raise ValueError('La fecha ingresada no corresponde al formato (DD/MM/AAAA)')
        if not(0<int(dia)<32):
            raise ValueError('Se ha ingresado un día no válido')
        if not(0<int(mes)<13):
            raise ValueError('Se ha ingresado un mes no válido')
        if not (dia.isdecimal() and mes.isdecimal() and anio.isdecimal()):
            raise ValueError('Solo se admiten números en la fecha')
        
        #convertir fecha a timestamp  
        self.fecha_nacimiento_formateada = f'{anio}-{mes}-{dia}'
        # print(f'El ciclista {self.nombre} se ha creado con exito')

  def convertir_a_lista(self):
    #num_inscripcion_ciclista, num_identificacion , nombre, apellido , strftime("%d/%m/%Y",fecha_de_nacimiento,"unixepoch") , pais,   num_equipo, ranking_UCI
    
    lista_ciclista = [self.num_identificacion, self.nombre, self.apellido, self.fecha_nacimiento_formateada, self.pais, self.num_equipo, self.ranking_UCI]

    if hasattr(self, 'num_inscripcion'):
      lista_ciclista.insert(0, self.num_inscripcion)
    
    return lista_ciclista
  