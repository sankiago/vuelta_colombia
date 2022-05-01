#Módulo 2 
#Gestion de inscripción - actualizacion de datos , de ciclitas en competencia 

import smtplib, ssl

def crear_ciclista(conexion, ciclista):
  """
  Función creación ciclista.
  Recibe un objeto Connection.
  Recibe una lista de la siguiente manera:
  [num_identificacion, nombre, apellido, fecha_nacimiento, pais, num_equipo,ranking_UIC]
  """
  cursor              = conexion.cursor()
  sentencia_insercion = 'INSERT INTO ciclistas(num_identificacion ,nombre ,apellido ,fecha_de_nacimiento ,pais ,num_equipo ,ranking_UIC) VALUES(?,?,?,?,?,?,?)'
  cursor.execute(sentencia_insercion, ciclista)
  conexion.commit()


def actualizar_ranking_UIC(conexion, id_ciclista, nuevo_ranking_UIC):
    """
    Función actualización ranking UIC.
    Recibe el número del ciclista pra la actualización del ranking UIC (num_identificacion).
    Recibe el nuevo ranking UIC.
    """
    cursor                  = conexion.cursor()
    sentencia_actualizacion = f'UPDATE ciclistas SET ranking_UIC = {nuevo_ranking_UIC} WHERE num_inscripcion_ciclista = {id_ciclista}'
    cursor.execute(sentencia_actualizacion)
    conexion.commit()


def consultar_info_vigente(conexion):
  """
  Función consultar informacion viegente.
  Recibe un objeto Connection (conexion).
  """
  cursor             = conexion.cursor()
  sentencia_consulta = f'SELECT * FROM ciclistas'
  respuesta_consulta = cursor.execute(sentencia_consulta).fetchall()
  return respuesta_consulta

