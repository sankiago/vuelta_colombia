from logica.modulo_3 import crear_etapa, actualizar_info_ciclista
from terminaltables import AsciiTable
from logica.modulo_1 import consultar_equipo_por_id


def crear_etapa_user(conexion):
    '''
    Funcion crear etapa
    recibe un objeto conexion
    y devuelve los parametros (conexion, info_etapa)
    '''
    print('Ingrese los datos del ciclista:')
    numero_etapa                        = input('Numero de la etapa: ')
    numero_inscripcion_ciclista         = input('Numero de inscripcion del ciclista: ')
    posicion_etapa                      = input('Posicion en la etapa: ')
    #Llave Primaria artificial
    etapa_ciclista                      = str(numero_etapa) + '-' + str(numero_inscripcion_ciclista)
    tiempo_empleado                     = input('Tiempo Empleado (HH:MM): ')

    horas, minutos = tiempo_empleado.split(':')
    if len(tiempo_empleado.split(':')) != 2 or (len(minutos) != 2):
        raise ValueError('El tiempo ingresado no corresponde al formato (HH:MM)')
    if not (horas.isdecimal() and minutos.isdecimal()):
        raise ValueError('Solo se admiten números en el formato (HH:MM)')
    tiempo_convertido = minutos
    minutos = horas*60
    tiempo_convertido = tiempo_convertido + minutos

    num_equipo                          = input('Número de equipo en el que corre: ')
    esta_retirado                       = input('¿El ciclista se retiro? Y/N: ')

    if  esta_retirado.upper()   == "Y" or esta_retirado.upper() == "YES":
        #Se evalua si el ciclista esta retirado o no
        retirado = 'Si'
    elif esta_retirado.upper()  == 'N' or esta_retirado.upper() == 'NO':
        retirado = 'No'

    if len(consultar_equipo_por_id(conexion, num_equipo)) == 0:
        #Evalua si el equipo al que se accede existe o no
        raise ValueError('El equipo seleccionado no existe')
       
    info_etapa                          = [numero_etapa, numero_inscripcion_ciclista, etapa_ciclista, posicion_etapa, tiempo_convertido, num_equipo, retirado]
    crear_etapa(conexion, info_etapa)
    print(f'La informacion de la etapa {numero_etapa} y ciclista {numero_inscripcion_ciclista} se ha creado con éxito')


def actualizar_info_ciclista_user(conexion):
    '''
    Funcion que actualiza la informacion del ciclista en la etapa.
    Recibe un objeto conexion.
    Y devuelve los parametros (conexion, nueva_posicion, num_ciclista, tiempo_convertido)
    '''
    num_ciclista        = input('Ingrese el número de inscripcion del ciclista : ')
    nueva_posicion      = input('Ingrese la nueva posicion del ciclista: ')
    nuevo_tiempo        = input('Ingrese el nuevo tiempo: ')
    horas, minutos      = nuevo_tiempo.split(':')

    if len(nuevo_tiempo.split(':')) != 2 or (len(minutos) != 2):
        #Se evalua si el formato de tiempo que digito el usuario es valido o no
        raise ValueError('El tiempo ingresado no corresponde al formato (HH:MM)')
    if not (horas.isdecimal() and minutos.isdecimal()):
        raise ValueError('Solo se admiten números en el formato (HH:MM)')
    tiempo_convertido = minutos
    minutos = horas*60
    tiempo_convertido = tiempo_convertido + minutos
    actualizar_info_ciclista(conexion, nueva_posicion, num_ciclista, tiempo_convertido)
    print(f'El tiempo del ciclista con número de inscripción {num_ciclista} ha sido actualizado.')
