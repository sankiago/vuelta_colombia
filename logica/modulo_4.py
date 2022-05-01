# Módulo 4: Consulta de clasificaciones

from logica.init_db  import conexion_a_la_db

conexion = conexion_a_la_db()

#Consulta individual por etapa

def consulta_ciclista_ID_etapa(conexion,ID):
	'''
	Función consulta individual por etapa.
	Recibe un objeto conexión.
	Recibe la identificación única del ciclista.
	Consulta la informacion de un ciclista mediante su ID única para una etapa determinada
	'''
	cursor = conexion.cursor()
	
