# Módulo 4: Consulta de clasificaciones
#Consulta individual por etapa

from modelos import Resultado

class Resultado_DAO:
	@staticmethod
	def consulta_etapa(conexion,num_etapa,orden=None):
		'''
		Función consulta por etapa.
		Recibe un objeto conexión.
		Recibe el parámetro de orden de tabla.
		Consulta la informacion de la clasificación de la etapa, ordenada según el parámetro recibido
		'''
		if orden == None:
			orden = "tiempo_empleado"
		cursor = conexion.cursor()
		sentencia_consulta = f'''SELECT clasificacion.num_etapa,
		ciclistas.num_inscripcion_ciclista,
		ciclistas.nombre,
		ciclistas.apellido,
		ciclistas.pais,
		equipos.nombre AS nombre_equipo,
		clasificacion.tiempo_empleado
		FROM ciclistas 
		INNER JOIN equipos ON  ciclistas.num_equipo = equipos.num_equipo 
		INNER JOIN clasificacion ON ciclistas.num_inscripcion_ciclista = clasificacion.num_ciclista AND clasificacion.num_etapa = {num_etapa}
		ORDER BY {orden}'''
		respuesta = cursor.execute(sentencia_consulta)
		etapa = [Resultado(tupla) for tupla in respuesta]
		return etapa

	@staticmethod
	def consulta_general(conexion,orden=None):
		'''
		Función consulta de la clasificación general.
		Recibe un objeto conexión.
		Recibe el parámetro de orden de la tabla.
		Consulta la informacion de la clasificación general de la carrera, ordenada según el parámetro recibido
		'''
		if orden == None:
			orden = "tiempo_empleado"
		cursor = conexion.cursor()

		sentencia_consulta = f'''SELECT 
				ciclistas.num_inscripcion_ciclista,
				ciclistas.nombre,
				ciclistas.apellido,
				ciclistas.pais,
				equipos.nombre AS nombre_equipo,
				SUM(clasificacion.tiempo_empleado) AS "Tiempo total"
				FROM ciclistas 
				INNER JOIN equipos ON  ciclistas.num_equipo = equipos.num_equipo 
				INNER JOIN clasificacion ON ciclistas.num_inscripcion_ciclista = clasificacion.num_ciclista 
				GROUP BY ciclistas.num_inscripcion_ciclista
				ORDER BY {orden} 
				'''
		respuesta = cursor.execute(sentencia_consulta)
		clasificacion = [Resultado(tupla) for tupla in respuesta] #:v
		return clasificacion