

class Etapa():
    def __init__(self, lista_de_informacion=None, num_equipo=None, numero_etapa= None, numero_inscripcion_ciclista=None, numero_etapa_numero_ciclista=None,posicion_etapa=None, tiempo_empleado=None, esta_retirado=None):
        
        if lista_de_informacion != None:
                self.numero_etapa, self.numero_inscripcion_ciclista, self.posicion_etapa, self.etapa_ciclista, self.tiempo_empleado, self.tiempo_convertido = lista_de_informacion
        else:
            print('Ingrese los datos del ciclista:')
            self.numero_etapa                   = numero_etapa
            self.numero_inscripcion_ciclista    = numero_inscripcion_ciclista
            self.posicion_etapa                 = posicion_etapa
            #Llave Primaria artificial
            self.numero_etapa_numero_ciclista   = str(numero_etapa) + '-' + str(numero_inscripcion_ciclista)
            self.num_equipo                     = num_equipo
            #self.esta_retirado                  = esta_retirado

            horas, minutos = tiempo_empleado.split(':')
            if len(tiempo_empleado.split(':')) != 2 or (len(minutos) != 2):
                raise ValueError('El tiempo ingresado no corresponde al formato (HH:MM)')
            if not (horas.isdecimal() and minutos.isdecimal()):
                raise ValueError('Solo se admiten números en el formato (HH:MM)')

            horas_en_minutos = int(horas)*60
            self.tiempo_convertido = horas_en_minutos + int(minutos)

            
            if  esta_retirado.upper()   == "Y" or esta_retirado.upper() == "YES":
                #Se evalua si el ciclista esta retirado o no
                self.esta_retirado = 'Si'
            elif esta_retirado.upper()  == 'N' or esta_retirado.upper() == 'NO':
                self.esta_retirado = 'No'
            
    def convertir_a_lista(self):
        lista_etapa = [self.numero_etapa, self.numero_inscripcion_ciclista, self.numero_etapa_numero_ciclista, self.posicion_etapa,self.tiempo_convertido, self.num_equipo, self.esta_retirado]
        #num_etapa, num_ciclista, num_etapa_num_ciclista, posicion_etapa , tiempo_empleado ,num_equipo , esta_retirado )
        return lista_etapa
            