from terminaltables import AsciiTable
from logica.modulo_4 import consulta_etapa,consulta_general
from pick import pick

def consulta_etapa_user(conexion):
	etapa = input('Ingrese la etapa a consultar:	')
	opciones = ['Tiempo','Idenficacion', 'Equipo', 'Nombre', 'Apellido', 'País']
	campo_SQL = {
		'Tiempo':  'tiempo_empleado',
		'Identificación' : 'num_inscripcion_ciclista',
		'Equipo' : 'nombre_equipo',
		'Nombre' : 'nombre',
		'Apellido' : 'apellido',
		'País' : 'pais'
	}
	orden = pick(opciones,'¿De acuerdo a qué parámetro debería estar ordedenada la consulta?')[0]
	parametro_seleccionado = campo_SQL[orden]
	#if orden.upper() == 'TIEMPO' or orden.upper() == 'T':
	#	orden = 'tiempo_empleado'
	#elif orden.upper()=='ID' or orden.upper()=='IDENTIFICACION CICLISTA' or orden.upper()=='IDENTIFICACION' or orden.upper() == #'IDENTIFICACIÓN' or orden.upper()=='IDENTIFICACIÓN CICISTA':
	#	orden = 'num_inscripcion_ciclista'
	#elif orden.upper()=='E' or orden.upper()=='EQUIPO' or orden.upper=='EQUIPO CICLISTA':
	#	orden = 'nombre_equipo'
	#else:
	#	raise ValueError('Parámetro Inválido')
	consulta = consulta_etapa(conexion,etapa,parametro_seleccionado)
	contador = 0
	resultado = []
	for tupla in consulta:
		resultado[contador] = list(tupla)
		contador += 1

	contador = 0	
	while contador < len(resultado):
		minutos_total =	resultado[contador][6]
		horas = minutos_total//60
		minutos = minutos_total%60
		hh_mm = f'{horas}:{minutos}'
		resultado[contador][6] = hh_mm

	encabezados_de_la_tabla = [['Etapa', 'Número de ID de Ciclista', 'Nombre', 'Apellido', 'Pais de origen','Nombre del Equipo en el que corre', 'Tiempo Empleado (HH:MM)']]
	datos_de_la_tabla = encabezados_de_la_tabla + resultado
	tabla_ciclista = AsciiTable(datos_de_la_tabla)
	tabla_ciclista.title= 'Consulta de información de Etapa'
	print(tabla_ciclista.table)

def consulta_general_user(conexion):
	opciones = ['Tiempo','Idenficacion', 'Equipo', 'Nombre', 'Apellido', 'País']
	campo_SQL = {
		'Tiempo':  'tiempo_empleado',
		'Identificación' : 'num_inscripcion_ciclista',
		'Equipo' : 'nombre_equipo',
		'Nombre' : 'nombre',
		'Apellido' : 'apellido',
		'País' : 'pais'
	}
	orden = pick(opciones,'¿De acuerdo a qué parámetro debería estar ordedenada la consulta?')[0]
	parametro_seleccionado = campo_SQL[orden]

	consulta = consulta_general(conexion,parametro_seleccionado)
	contador = 0
	resultado = []
	for tupla in consulta:
		resultado[contador] = list(tupla)
		contador += 1

	contador = 0	
	while contador < len(resultado):
		minutos_total =	resultado[contador][5]
		horas = minutos_total//60
		minutos = minutos_total%60
		hh_mm = f'{horas}:{minutos}'
		resultado[contador][5] = hh_mm

	encabezados_de_la_tabla = [['Número de ID de Ciclista', 'Nombre', 'Apellido', 'Pais de origen','Nombre del Equipo en el que corre', 'Tiempo Empleado (HH:MM)']]
	datos_de_la_tabla = encabezados_de_la_tabla + resultado
	tabla_ciclista = AsciiTable(datos_de_la_tabla)
	tabla_ciclista.title= 'Consulta de información de Clasificación General'
	print(tabla_ciclista.table)
	
