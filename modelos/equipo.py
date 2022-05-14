import re


class Equipo():
    def __init__(self, nombre, pais, director, marca_bicicleta, marca_ciclocomputador, direccion_sede_central, telefono, correo_electronico, num_equipo=None):
        if num_equipo != None:
            self.num_equipo = num_equipo

        self.nombre = nombre
        self.pais = pais
        self.director = director
        self.marca_bicicleta = marca_bicicleta
        self.marca_ciclocomputador = marca_ciclocomputador
        self.direccion_sede_central = direccion_sede_central
        self.telefono = telefono
        self.correo_electronico = correo_electronico
        print(f'El equipo {self.nombre} se ha creado con éxito')

        patron_numero_de_telefono = r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$'
        patron_correo_electronico = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        correo_de_electronico_es_valido = not bool(
            re.fullmatch(patron_correo_electronico, correo_electronico))
        numero_de_telefono_es_valido = not bool(
            re.fullmatch(patron_numero_de_telefono, telefono))

        if correo_de_electronico_es_valido:
            raise ValueError(f'el número de teléfono {telefono} no es válido')
        if numero_de_telefono_es_valido:
            raise ValueError(
                f'la dirección de correo {correo_electronico} no válida')

    def convertir_a_lista(self):
        lista_equipo = [self.nombre, self.pais, self.director, self.marca_bicicleta,
                        self.marca_ciclocomputador, self.direccion_sede_central, self.telefono, self.correo_electronico]
        if self.num_equipo != None:
            lista_equipo.insert(0,self.num_equipo)
