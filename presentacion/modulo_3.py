from logica.modulo_3 import crear_etapa, actualizar_info_ciclista
from terminaltables import AsciiTable
from logica.modulo_1 import consultar_equipo_por_id


def crear_etapa_user(conexion):
    print('Ingrese los datos del ciclista:')
    numero_etapa                        = input('Numero de la etapa: ')
    numero_inscripcion_ciclista         = input('Numero de inscripcion del ciclista: ')
    posicion_etapa                      = input('Posicion en la etapa: ')
    #Llave Primaria artificial
    etapa_ciclista                      = str(numero_etapa) + '-' + str(numero_inscripcion_ciclista)
    tiempo_empleado                     = input('Tiempo Empleado (HH:MM): ')
    num_equipo                          = input('Número de equipo en el que corre: ')
    esta_retirado                       = input('¿El ciclista se retiro? Y/N: ')

    if  esta_retirado.upper() == "Y" or esta_retirado.upper() == "YES":
        retirado = 'Si'
    elif esta_retirado.upper() == 'N' or esta_retirado.upper() == 'NO':
        retirado = 'No'
    """elif esta_retirado.upper() != 'Y' or 'YES' or 'N' or 'NO':
        etapa_ciclista = input('Digite una entrada valida Y/N')
        if  esta_retirado.upper() == "Y" or "YES":
            esta_retirado = 'Si'
        elif esta_retirado.upper() == 'N' or 'NO':
            esta_retirado = 'No'"""

    if len(consultar_equipo_por_id(conexion, num_equipo)) == 0:
        raise ValueError('El equipo seleccionado no existe')
       
    info_etapa                          = [numero_etapa, numero_inscripcion_ciclista, etapa_ciclista, posicion_etapa, tiempo_empleado, num_equipo, retirado]
    crear_etapa(conexion, info_etapa)
    print(f'La informacion de la etapa {numero_etapa} y ciclista {numero_inscripcion_ciclista} se ha creado con éxito')


def actualizar_info_ciclista_user(conexion):
    num_ciclista        = input('Ingrese el número de inscripcion del ciclista : ')
    nueva_posicion      = input('Ingrese la nueva posicion del ciclista: ')
    nuevo_tiempo        = input('Ingrese el nuevo tiempo: ')
    actualizar_info_ciclista(conexion, nueva_posicion, num_ciclista, nuevo_tiempo)
    print(f'El tiempo del ciclista con número de inscripción {num_ciclista} ha sido actualizado.')
