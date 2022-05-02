from terminaltables import AsciiTable
from logica.modulo_4 import consulta_etapa

def consulta_etapa_user(conexion):
	etapa = input('Ingrese la etapa a consultar:	')
	orden = input('¿De acuerdo a qué debería estar ordenada la consulta?:	')
	if orden.upper() == 'TIEMPO' or orden.upper() == 'T':
		orden = 'tiempo_empleado'
	elif orden.upper()=='ID' or orden.upper()=='IDENTIFICACION CICLISTA' or orden.upper()=='IDENTIFICACION' or orden.upper() == 'IDENTIFICACIÓN' or orden.upper()=='IDENTIFICACIÓN CICISTA':
		orden = 'num_inscripcion_ciclista'
	elif orden.upper()=='E' or orden.upper()=='EQUIPO' or orden.upper=='EQUIPO CICLISTA':
		orden = 'nombre_equipo'
	else:
		raise ValueError('Parámetro Inválido')

def consulta_general_user(conexion):
	
	
	return