from logica         import CiclistaDAO
from modelos        import Ciclista
from terminaltables import AsciiTable

def crear_ciclista_user(conexion):
    '''
    Funcion que toma los datos del ciclista para luego enviarlos a la parte logica
    Recibe conexion como objeto y envia dos parametros a dos funciones diferentes
    '''
    print('Ingrese los datos del ciclista participante.')
    num_identificacion = input('        Número de identificación: ')
    nombre             = input('                          Nombre: ')
    apellido           = input('                        Apellido: ')
    fecha_nacimiento   = input('Fecha de nacimiento (DD/MM/AAAA): ') 
    pais               = input('                  Pais de origen: ')
    num_equipo         = input('Número de equipo en el que corre: ')
    ranking_UCI        = input('                     Ranking UCI: ')
    # sin implementar:
    # fotografia             = input('Fotografía: ')
    ciclista = Ciclista(num_identificacion=num_identificacion, nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, pais=pais, num_equipo=num_equipo, ranking_UCI=ranking_UCI) 
    CiclistaDAO.crear_ciclista(conexion, ciclista)
    print(f'El ciclista {nombre} se ha registrado con éxito')  

def cambiar_ranking_UIC_user(conexion):
    '''Se cambia la informacion de fue digitada en un principio en la columna de Ranking UCI'''
    num_ciclista        = input('Ingrese el número de inscripcion del ciclista : ')
    nuevo_ranking_UIC   = input('                  Ingrese el nuevo ranking UCI: ')
    CiclistaDAO.actualizar_ranking_UIC(conexion, num_ciclista, nuevo_ranking_UIC)
    print(f'El ranking UCI del ciclista con número de inscripción {num_ciclista} ha sido actualizado.')

def consultar_info_vigente_user(conexion):
    ciclistas = CiclistaDAO.consultar_info_vigente(conexion)
    if ciclistas == None:
        print(f'No se ha encontrado información')
    else:
        cuerpo_de_la_tabla      = [ciclista.convertir_a_lista() for ciclista in ciclistas]
        encabezados_de_la_tabla = [['Número de inscripción', 'Número de identificación', 'Nombre', 'Apellido', 'Fecha de nacimiento (DD/MM/AAAA)', 'Pais de origen','Número de equipo en el que corre', 'Ranking UCI']]
        datos_de_la_tabla       = encabezados_de_la_tabla + cuerpo_de_la_tabla
        tabla_ciclista          = AsciiTable(datos_de_la_tabla)
        tabla_ciclista.title    = ' Consulta de información vigente '
        print(tabla_ciclista.table)

def consultar_info_vigente_ciclista_user(conexion):
    num_ciclista = input('Ingrese el número de inscripción del ciclista a consultar: ')
    ciclista = CiclistaDAO.consultar_info_vigente_ciclista(conexion, num_ciclista)
    if ciclista == None:
        print(f'No se ha encontrado información')
    else:
        cuerpo_de_la_tabla      = [ciclista.convertir_a_lista()] 
        encabezados_de_la_tabla = [['Número de inscripción', 'Número de identificación', 'Nombre', 'Apellido', 'Fecha de nacimiento (DD/MM/AAAA)', 'Pais de origen','Número de equipo en el que corre', 'Ranking UCI']]
        datos_de_la_tabla       = encabezados_de_la_tabla + cuerpo_de_la_tabla
        tabla_ciclista          = AsciiTable(datos_de_la_tabla)
        tabla_ciclista.title    = ' Consulta de ciclista '
        print(tabla_ciclista.table)