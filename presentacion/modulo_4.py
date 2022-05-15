from terminaltables import AsciiTable
from logica import Resultado_DAO 

from pick import pick

from modelos.resultado import Resultado

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

	etapa = Resultado_DAO.consulta_etapa(conexion,etapa,parametro_seleccionado)
	cuerpo_de_la_tabla = [resultado.convertir_a_lista() for resultado in etapa]

	encabezados_de_la_tabla = [['Etapa', 'Número de ID de Ciclista', 'Nombre', 'Apellido', 'Pais de origen','Nombre del Equipo en el que corre', 'Tiempo Empleado (HH:MM)']]
	datos_de_la_tabla = encabezados_de_la_tabla + cuerpo_de_la_tabla
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

	clasificacion_general = Resultado_DAO.consulta_general(conexion,parametro_seleccionado)
	cuerpo_de_la_tabla = [resultado.convertir_a_lista() for resultado in clasificacion_general]

	encabezados_de_la_tabla = [['Número de ID de Ciclista', 'Nombre', 'Apellido', 'Pais de origen','Nombre del Equipo en el que corre', 'Tiempo Empleado (HH:MM)']]
	datos_de_la_tabla = encabezados_de_la_tabla + cuerpo_de_la_tabla
	tabla_ciclista = AsciiTable(datos_de_la_tabla)
	tabla_ciclista.title= 'Consulta de información de Clasificación General'
	print(tabla_ciclista.table)
	
