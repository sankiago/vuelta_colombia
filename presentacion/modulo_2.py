from multiprocessing.sharedctypes import Value
from logica.modulo_1 import consultar_equipo_por_id
from logica.modulo_2 import crear_ciclista, actualizar_ranking_UIC, consultar_info_vigente
from terminaltables  import AsciiTable
from datetime        import datetime

from presentacion.modulo_3 import crear_etapa_user

def crear_ciclista_user(conexion):
    '''
    Funcion que toma los datos del ciclista para luego enviarlos a la parte logica
    Recibe conexion como objeto y envia dos parametros a dos funciones diferentes
    '''
    print('Ingrese los datos del ciclista participante.')
    num_identificacion     = input('Número de identificación: ')
    nombre                 = input('Nombre: ')
    apellido               = input('Apellido: ')
    fecha_nacimiento       = input('Fecha de nacimiento (DD/MM/AAAA): ')

    #verficar que la fecha cumpla el formato
    dia, mes, anio = fecha_nacimiento.split('/')
    if len(fecha_nacimiento.split('/')) != 3 or (len(dia) != 2 or len(mes) != 2 or len(anio) != 4):
        raise ValueError('La fecha ingresada no corresponde al formato (DD/MM/AAAA)')
    if not(0<int(dia)<32):
        raise ValueError('Se ha ingresado un día no válido')
    if not(0<int(mes)<13):
        raise ValueError('Se ha ingresado un mes no válido')
    
    if not (dia.isdecimal() and mes.isdecimal() and anio.isdecimal()):
        raise ValueError('Solo se admiten números en la fecha')

    pais                   = input('Pais de origen: ')
    num_equipo             = input('Número de equipo en el que corre: ')
    #Validando si el equipo existe
    if len(consultar_equipo_por_id(conexion, num_equipo)) == 0:
        raise ValueError('El equipo seleccionado no existe')

    #sin implementar: fotografia             = input('Fotografía: ')
    ranking_UIC            = input('Ranking UCI: ')
    
    #convertir fecha a timestamp
    fecha_nacimiento_timestamp = datetime(int(anio), int(mes), int(dia)).timestamp()
    print(fecha_nacimiento_timestamp)
    ciclista               = [num_identificacion ,nombre ,apellido ,fecha_nacimiento_timestamp ,pais ,num_equipo ,ranking_UIC]
    
    crear_ciclista(conexion, ciclista)
    crear_etapa_user(conexion, ciclista)
    print(f'El ciclista {nombre} se ha registrado con éxito')
    

def cambiar_ranking_UIC_user(conexion):
    '''Se cambia la informacion de fue digitada en un principio en la columna de Ranking UIC'''
    num_ciclista        = input('Ingrese el número de inscripcion del ciclista : ')
    nuevo_ranking_UIC   = input('Ingrese el nuevo ranking UIC: ')
    actualizar_ranking_UIC(conexion, num_ciclista, nuevo_ranking_UIC)
    print(f'El ranking UIC del ciclista con número de inscripción {num_ciclista} ha sido actualizado.')


def consultar_info_vigente_user(conexion):
    respuesta_consulta = consultar_info_vigente(conexion)
    if len(respuesta_consulta) == 0:
        print(f'No se ha encontrado información')
    else:
        ciclistas = [list(ciclista) for ciclista in respuesta_consulta]
        #convirtiendo unixtime en DD/MM/AAA
        for ciclista in ciclistas:
            #ciclisa[4] es el unixtime que devuelve la db
            
            ciclista[4] = datetime.utcfromtimestamp(ciclista[4]).strftime('%d/%m/%Y')
       
        

        encabezados_de_la_tabla = [['Número de inscripción', 'Número de identificación', 'Nombre', 'Apellido', 'Fecha de nacimiento (DD/MM/AAAA)', 'Pais de origen','Número de equipo en el que corre', 'fotografia', 'Ranking UCI']]
        datos_de_la_tabla       = encabezados_de_la_tabla + ciclistas
        tabla_ciclista          = AsciiTable(datos_de_la_tabla)
        tabla_ciclista.title    = ' Consulta de información vigente '
        print(tabla_ciclista.table)