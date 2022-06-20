from logica  import EquipoDAO
from modelos import Ciclista

class CiclistaDAO:    
    @staticmethod
    def crear_ciclista(conexion, ciclista):
      """
      Función creación ciclista.
      Recibe un objeto Connection.
      Recibe una lista de la siguiente manera:
      [num_identificacion, nombre, apellido, fecha_nacimiento, pais, num_equipo,ranking_UIC]
      """

      #Validando si el equipo del ciclista existe
      if EquipoDAO.consultar_equipo_por_id(conexion, ciclista.num_equipo) == None:
          raise ValueError('El equipo seleccionado no existe')
      
      cursor              = conexion.cursor()
      sentencia_insercion = """
      INSERT INTO
         ciclistas(
          num_identificacion,
          nombre,
          apellido,
          fotografia,
          fecha_de_nacimiento,
          pais,
          num_equipo,
          ranking_UIC
          )
      VALUES
      (?,?,?,strftime("%s", ?),?,?,?)"""
      cursor.execute(sentencia_insercion, ciclista.convertir_a_lista())
      conexion.commit()
            
    @staticmethod
    def actualizar_pais(conexion, id_ciclista, nuevo_pais):
      """
      Función actualización Pais.
      Recibe el número del ciclista pra la actualización del pais (num_identificacion).
      Recibe el nuevo país.
      """
      cursor                  = conexion.cursor()
      sentencia_actualizacion = f"""
      UPDATE
        ciclistas
      SET
        pais = '{nuevo_pais}'
      WHERE 
        num_inscripcion_ciclista = {id_ciclista}
      """
      cursor.execute(sentencia_actualizacion)
      conexion.commit()

    @staticmethod
    def buscar_en_todos_los_campos(conexion, cadena_de_busqueda):
      cursor             = conexion.cursor()
      print(cadena_de_busqueda)
      sentencia_consulta = f"""
      SELECT 
        num_inscripcion_ciclista,
        num_identificacion,
        nombre,
        apellido,
        fotografia,
        strftime("%d/%m/%Y",fecha_de_nacimiento,"unixepoch"),
        pais,
        num_equipo,
        ranking_UIC 
      FROM 
        ciclistas
      WHERE
      
           (REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(num_inscripcion_ciclista,'á','a'),'é','e' ),'í','i'),'ó','o'),'ú','u') = '{cadena_de_busqueda}' COLLATE NOCASE )
        OR (REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(num_identificacion,'á','a'),'é','e' ),'í','i'),'ó','o'),'ú','u') = '{cadena_de_busqueda}' COLLATE NOCASE )
        OR (REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(nombre,'á','a'),'é','e' ),'í','i'),'ó','o'),'ú','u') = '{cadena_de_busqueda}' COLLATE NOCASE )
        OR (REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(apellido,'á','a'),'é','e' ),'í','i'),'ó','o'),'ú','u') = '{cadena_de_busqueda}' COLLATE NOCASE) 
        OR (REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(nombre || ' ' || apellido,'á','a'),'é','e' ),'í','i'),'ó','o'),'ú','u') = '{cadena_de_busqueda}' COLLATE NOCASE )
        OR (REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(fotografia,'á','a'),'é','e' ),'í','i'),'ó','o'),'ú','u') = '{cadena_de_busqueda}' COLLATE NOCASE )
        OR (REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(strftime("%d/%m/%Y",fecha_de_nacimiento,"unixepoch"),'á','a'),'é','e' ),'í','i'),'ó','o'),'ú','u') = '{cadena_de_busqueda}' COLLATE NOCASE )
        OR (REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(pais,'á','a'),'é','e' ),'í','i'),'ó','o'),'ú','u') = '{cadena_de_busqueda}' COLLATE NOCASE )
        OR (REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(num_equipo,'á','a'),'é','e' ),'í','i'),'ó','o'),'ú','u') = '{cadena_de_busqueda}' COLLATE NOCASE )
        OR (REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(ranking_UIC,'á','a'),'é','e' ),'í','i'),'ó','o'),'ú','u') = '{cadena_de_busqueda}' COLLATE NOCASE)
      """
      respuesta_consulta = cursor.execute(sentencia_consulta).fetchall()
      lista_ciclistas    = [Ciclista(tupla) for tupla in respuesta_consulta]
      return lista_ciclistas

    @staticmethod
    #Necesita que el parametro_orden esté limpio (que aparezca tal cual como en la base de datos) para que funcione, pues de no ser así, arrojará un error
    def consultar_todos_los_ciclistas(conexion,parametro_orden=None):
      """
      Función consultar todos los ciclistas.
      Recibe un objeto conexión (conexion).
      Recibe el parámetro por el cual se ordenará la consulta (parametro_orden).
      """

      campos = ['num_inscripcion_ciclista','num_identificacion','nombre','apellido','fecha_de_nacimiento','pais','num_equipo','fotografia','ranking_UIC']
      if (parametro_orden == None) or (parametro_orden not in campos):
        parametro_orden = 'nombre'
      cursor            = conexion.cursor()
      sentencia_consulta = f''' 
      SELECT
        num_inscripcion_ciclista,
        num_identificacion,
        nombre,
        apellido,
        fotografia,
        strftime("%d/%m/%Y",fecha_de_nacimiento,"unixepoch"),
        pais,
        num_equipo,
        ranking_UIC
		  FROM
        ciclistas 
		  ORDER BY
        {parametro_orden}
      '''
      respuesta_consulta = cursor.execute(sentencia_consulta).fetchall()
      lista_ciclistas    = [Ciclista(tupla) for tupla in respuesta_consulta]
      return lista_ciclistas

    @staticmethod
    def eliminar_ciclista_por_id(conexion,ID_ciclista):
      """
      Función eliminar ciclista por ID.
      Recibe un objeto conexión (conexion).
      Recibe el ID del ciclista a eliminar (ID_ciclista).
      """
      cursor            = conexion.cursor()
      sentencia_consulta = f'''DELETE FROM ciclistas WHERE num_inscripcion_ciclista = {ID_ciclista}'''
      cursor.execute(sentencia_consulta)

            
      pass

    @staticmethod
    def consultar_ciclista(conexion, num_ciclista):
      """
      Función consultar informacion viegente.
      Recibe un objeto Connection     (conexion).
      Recibe el número de inscripción (num_ciclista).
      """
      cursor             = conexion.cursor()
      #sentencia_consulta = f'SELECT num_inscripcion_ciclista, num_identificacion , nombre, apellido , strftime("%d/%m/%Y",fecha_de_nacimiento,"unixepoch") , pais,   num_equipo, ranking_UIC FROM ciclistas WHERE num_inscripcion_ciclista = {num_ciclista}'
      sentencia_consulta = f'SELECT num_inscripcion_ciclista, num_identificacion , nombre, apellido ,fotografia, strftime("%d/%m/%Y",fecha_de_nacimiento,"unixepoch") , pais,   num_equipo, ranking_UIC FROM ciclistas WHERE num_inscripcion_ciclista = {num_ciclista}'
      respuesta_consulta = cursor.execute(sentencia_consulta).fetchall()
      if len(respuesta_consulta) == 0:
        ciclista = None
      else:
        ciclista = Ciclista(respuesta_consulta[0])
      return ciclista