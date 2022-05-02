# Módulo 4: Consulta de clasificaciones
#Consulta individual por etapa



def consulta_etapa(conexion,etapa,orden):
	'''
	Función consulta por etapa.
	Recibe un objeto conexión.
	Recibe el parámetro de orden de tabla.
	Consulta la informacion de la clasificación de la etapa, ordenada según el parámetro recibido
	'''
	
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
	INNER JOIN clasificacion ON ciclistas.num_inscripcion_ciclista = clasificacion.num_ciclista AND clasificacion.num_etapa = {etapa}
	ORDER BY {orden}'''
	consulta = cursor.execute(sentencia_consulta)

	return consulta

def consulta_general(conexion,orden):
	'''
	Función consulta de la clasificación general.
	Recibe un objeto conexión.
	Recibe el parámetro de orden de la tabla.
	Consulta la informacion de la clasificación general de la carrera, ordenada según el parámetro recibido
	'''
	cursor = conexion.cursor()
	sentencia_consulta = f''
	if orden == 'tiempo_empleado':
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
			ORDER BY {orden} DESC
			'''
	else:
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
	consulta = cursor.execute(sentencia_consulta)
	return consulta