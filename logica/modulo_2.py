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
      sentencia_insercion = 'INSERT INTO ciclistas(num_identificacion ,nombre ,apellido ,fecha_de_nacimiento ,pais ,num_equipo ,ranking_UIC) VALUES(?,?,?,strftime("%s", ?),?,?,?)'
      cursor.execute(sentencia_insercion, ciclista.convertir_a_lista())
      conexion.commit()
      
      
    @staticmethod
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

    @staticmethod
    def consultar_info_vigente(conexion):
      """
      Función consultar informacion viegente.
      Recibe un objeto Connection (conexion).
      """
      cursor             = conexion.cursor()
      sentencia_consulta = f'SELECT num_inscripcion_ciclista, num_identificacion , nombre, apellido, fotografia , strftime("%d/%m/%Y",fecha_de_nacimiento,"unixepoch") , pais,   num_equipo, ranking_UIC FROM ciclistas'
      respuesta_consulta = cursor.execute(sentencia_consulta).fetchall()
      lista_ciclistas    = [Ciclista(tupla) for tupla in respuesta_consulta]
      return lista_ciclistas
    
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
    def consultar_info_vigente_ciclista(conexion, num_ciclista):
      """
      Función consultar informacion viegente.
      Recibe un objeto Connection     (conexion).
      Recibe el número de inscripción (num_ciclista).
      """
      cursor             = conexion.cursor()
      #sentencia_consulta = f'SELECT num_inscripcion_ciclista, num_identificacion , nombre, apellido , strftime("%d/%m/%Y",fecha_de_nacimiento,"unixepoch") , pais,   num_equipo, ranking_UIC FROM ciclistas WHERE num_inscripcion_ciclista = {num_ciclista}'
      sentencia_consulta = f'SELECT num_inscripcion_ciclista, num_identificacion , nombre, apellido , strftime("%d/%m/%Y",fecha_de_nacimiento,"unixepoch") , pais,   num_equipo, ranking_UIC FROM ciclistas WHERE num_inscripcion_ciclista = {num_ciclista}'
      respuesta_consulta = cursor.execute(sentencia_consulta).fetchall()
      if len(respuesta_consulta) == 0:
        ciclista = None
      else:
        ciclista = Ciclista(respuesta_consulta[0])
      return ciclista