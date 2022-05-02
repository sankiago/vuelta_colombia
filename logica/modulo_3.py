#Módulo 3
#Gestion de informacion de etapas e informacion por ciclista en la etapa

from multiprocessing.sharedctypes import Value
import smtplib, ssl
import re
def crear_etapa(conexion, info_etapa):
  """
  Función creación ciclista.
  Recibe un objeto Connection.
  Recibe una lista de la siguiente manera:
  [num_identificacion, nombre, apellido, fecha_nacimiento, pais, num_equipo,ranking_UIC]
  """


  cursor              = conexion.cursor()
  sentencia_insercion = 'INSERT INTO clasificacion(num_etapa, num_ciclista, num_etapa_num_ciclista, posicion_etapa , tiempo_empleado ,num_equipo , retirado ) VALUES(?,?,?,?,?,?,?)'
  cursor.execute(sentencia_insercion, info_etapa)
  conexion.commit()



def actualizar_info_ciclista(conexion, nueva_posicion, num_ciclista, nuevo_tiempo):
    """Funcion que se encarga de actualizar la informacion del ciclista en caso de que exista una equivocacion/error"""
    cursor                  = conexion.cursor()
    sentencia_actualizacion = f'UPDATE clasificacion SET posicion_etapa={nueva_posicion},tiempo_empleado = "{nuevo_tiempo}" WHERE num_ciclista = {num_ciclista}'
    cursor.execute(sentencia_actualizacion)
    conexion.commit()

