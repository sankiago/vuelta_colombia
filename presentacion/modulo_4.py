from terminaltables import AsciiTable
from logica.modulo_4 import consulta_etapa,consulta_general
from pick import pick

def consulta_etapa_user(conexion):
	etapa = input('Ingrese la etapa a consultar:	')
	opciones = ['Tiempo','Identificación', 'Equipo', 'Nombre', 'Apellido', 'País']
	campo_SQL = {
		'Tiempo':  'tiempo_empleado',
		'Identificación' : 'num_inscripcion_ciclista',
		'Equipo' : 'nombre_equipo',
		'Nombre' : 'ciclistas.nombre',
		'Apellido' : 'ciclistas.apellido',
		'País' : 'pais'
	}
	orden = pick(opciones,'¿De acuerdo a qué parámetro debería estar ordedenada la consulta?')[0]
	parametro_seleccionado = campo_SQL[orden]

	consulta = consulta_etapa(conexion,etapa,parametro_seleccionado)
	contador = 0
	resultado = [list(tupla) for tupla in consulta]


	contador = 0	
	while contador < len(resultado):
		minutos_total =	int(resultado[contador][6])
		horas = minutos_total//60
		minutos = minutos_total%60
		if len(str(minutos)) == 1:
			minutos = "0"+str(minutos)
		hh_mm = f'{horas}:{minutos}'
		resultado[contador][6] = hh_mm
		contador +=1

	encabezados_de_la_tabla = [['Etapa', 'Número de ID de Ciclista', 'Nombre', 'Apellido', 'Pais de origen','Nombre del Equipo en el que corre', 'Tiempo Empleado (HH:MM)']]
	datos_de_la_tabla = encabezados_de_la_tabla + resultado
	tabla_ciclista = AsciiTable(datos_de_la_tabla)
	tabla_ciclista.title= 'Consulta de información de Etapa'
	print(tabla_ciclista.table)

def consulta_general_user(conexion):
	opciones = ['Tiempo','Identificación', 'Equipo', 'Nombre', 'Apellido', 'País']
	campo_SQL = {
		'Tiempo':  '"Tiempo total"',
		'Identificación' : 'num_inscripcion_ciclista',
		'Equipo' : 'nombre_equipo',
		'Nombre' : 'ciclistas.nombre',
		'Apellido' : 'ciclistas.apellido',
		'País' : 'pais'
	}
	orden = pick(opciones,'¿De acuerdo a qué parámetro debería estar ordedenada la consulta?')[0]
	parametro_seleccionado = campo_SQL[orden]

	consulta = consulta_general(conexion,parametro_seleccionado)
	contador = 0
	resultado = [list(tupla) for tupla in consulta]

	contador = 0	
	while contador < len(resultado):
		minutos_total =	resultado[contador][5]
		horas = minutos_total//60
		minutos = minutos_total%60
		if len(str(minutos)) == 1:
			minutos = "0"+str(minutos)
		hh_mm = f'{horas}:{minutos}'
		resultado[contador][5] = hh_mm
		contador +=1

	encabezados_de_la_tabla = [['Número de ID de Ciclista', 'Nombre', 'Apellido', 'Pais de origen','Nombre del Equipo en el que corre', 'Tiempo Empleado (HH:MM)']]
	datos_de_la_tabla = encabezados_de_la_tabla + resultado
	tabla_ciclista = AsciiTable(datos_de_la_tabla)
	tabla_ciclista.title= 'Consulta de información de Clasificación General'
	print(tabla_ciclista.table)
	
