#Módulo 3
#Gestion de informacion de etapas e informacion por ciclista en la etapa

from multiprocessing.sharedctypes import Value
from sqlite3 import IntegrityError

class EtapaDAO:
  @staticmethod
  def crear_etapa(conexion, etapa):
    """
    Función creación ciclista.
    Recibe un objeto Connection.
    Recibe una lista de la siguiente manera:
    [numero_etapa, numero_inscripcion_ciclista, etapa_ciclista, posicion_etapa, tiempo_convertido, num_equipo, retirado]
    """

    cursor              = conexion.cursor()
    sentencia_insercion = 'INSERT INTO clasificacion(num_etapa, num_ciclista, num_etapa_num_ciclista, posicion_etapa , tiempo_empleado ,num_equipo , esta_retirado ) VALUES(?,?,?,?,?,?,?)'
    try:
      cursor.execute(sentencia_insercion, etapa.convertir_a_lista())
    except IntegrityError as error:
      raise ValueError(error)
    conexion.commit()

  @staticmethod 
  def consultar_num_etapas(conexion):
    cursor = conexion.cursor()
    sentencia_consulta = f'SELECT num_etapa FROM clasificacion GROUP BY num_etapa'
    resultado_consulta = cursor.execute(sentencia_consulta).fetchall()
    lista_etapas = [tupla[0] for tupla in resultado_consulta]
    return lista_etapas

  @staticmethod
  def actualizar_info_ciclista(self, conexion, nueva_posicion, num_ciclista, nuevo_tiempo):
      """
      Funcion que se encarga de actualizar la informacion del ciclista
      en caso de que exista una equivocacion/error
      """
      cursor                       = conexion.cursor()
      self.sentencia_actualizacion = f'UPDATE clasificacion SET posicion_etapa={nueva_posicion},tiempo_empleado = "{nuevo_tiempo}" WHERE num_ciclista = {num_ciclista}'
      cursor.execute(self.sentencia_actualizacion)
      conexion.commit()