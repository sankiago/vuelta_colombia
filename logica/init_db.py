#Se importaron las librerias necesarias
import sqlite3
from   sqlite3  import Error

#Función conexión base de datos con devolución objeto conexion
def conexion_a_la_db():
  try:
    conexion = sqlite3.connect('base_de_datos_vc.db')
    return conexion
  except Error:
    print(Error)

def crear_tablas(conexion):
  """
  Función creación de tablas.
  Recibe un objeto Connection
  """
  cursor = conexion.cursor()

  sentencia_equipos       = 'CREATE TABLE          equipos(num_equipo INTEGER PRIMARY KEY AUTOINCREMENT              , nombre TEXT                ,              pais_sede TEXT                         , director TEXT      , marca_bicicleta TEXT, marca_ciclocomputador TEXT,  direccion_sede_central TEXT,  telefono INTEGER,       correo_electronico TEXT)'
  sentencia_ciclistas     = 'CREATE TABLE        ciclistas(num_inscripcion_ciclista INTEGER PRIMARY KEY AUTOINCREMENT, num_identificacion INTEGER , nombre TEXT        , apellido TEXT       , fecha_de_nacimiento INTEGER, pais TEXT,   num_equipo INTEGER, fotografia TEXT, ranking_UIC TEXT, FOREIGN KEY(num_equipo) REFERENCES equipos(num_equipo))'
  sentencia_clasificacion = 'CREATE TABLE    clasificacion(num_etapa INTEGER                                         , num_ciclista INTEGER       , num_etapa_num_ciclista TEXT PRIMARY KEY, posicion_etapa TEXT, tiempo_empleado TEXT, num_equipo INTEGER, esta_retirado BOOLEAN, FOREIGN KEY(num_equipo) REFERENCES equipos(num_equipo), FOREIGN KEY(num_ciclista) REFERENCES ciclistas(num_inscripcion_ciclista))'     

  cursor.execute(sentencia_equipos)
  cursor.execute(sentencia_ciclistas)
  cursor.execute(sentencia_clasificacion)

  conexion.commit()

# diccionario_equipos = {
#   num_equipo, pais_sede, director, marca_bicicleta, marca_ciclocomputador,  direccion_sede_central,telefono,correo_electronico
# }

# SOLO PARA DEBUG!
def eliminar_tablas(conexion):
  """
  Función eliminación (si existen) de tablas.
  Recibe un objeto Connection
  """
  cursor = conexion.cursor()

  sentencia_equipos       = 'DROP TABLE IF EXISTS equipos'
  sentencia_ciclistas     = 'DROP TABLE IF EXISTS ciclistas'
  sentencia_clasificacion = 'DROP TABLE IF EXISTS clasificacion'     

  cursor.execute(sentencia_equipos)
  cursor.execute(sentencia_ciclistas)
  cursor.execute(sentencia_clasificacion)

  conexion.commit()
      
