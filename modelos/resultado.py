from modelos.modelo import Modelo

class Resultado(Modelo):
	def __init__(self, tupla_de_informacion):
		if len(tupla_de_informacion) == 7:
			self.num_etapa, self.num_inscripcion_ciclista, self.nombre_ciclista, self.apellido, self.pais, self.nombre_equipo, tiempo_empleado = tupla_de_informacion
		elif len(tupla_de_informacion) == 6:
			self.num_inscripcion_ciclista, self.nombre_ciclista, self.apellido, self.pais, self.nombre_equipo, tiempo_empleado = tupla_de_informacion
			self.num_etapa = None
		
		tiempo_empleado =	int(tiempo_empleado)
		horas = tiempo_empleado//60
		minutos = tiempo_empleado%60
		self.tiempo_convertido = f'{horas:02d}:{minutos:02d}'

	def convertir_a_lista(self):
		lista_clasificacion = [self.num_inscripcion_ciclista, self.nombre_ciclista, self.apellido, self.pais, self.nombre_equipo, self.tiempo_convertido] 
		if self.num_etapa != None:
			lista_clasificacion.insert(0,self.num_etapa)

		return lista_clasificacion
		
