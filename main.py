from   logica.init_db        import conexion_a_la_db, eliminar_tablas, crear_tablas
# from   logica                import *
from   logica import *
from   modelos.ciclista import Ciclista
import eel
import base64
#Inicializar base de datos
conexion = conexion_a_la_db('base_de_datos_vc.db')
crear_tablas(conexion)

@eel.expose
def consultar_todos_los_ciclistas(parametro_de_orden=None):
    ciclistas = CiclistaDAO.consultar_todos_los_ciclistas(conexion, parametro_de_orden)
    ciclistas_como_diccionarios = list(map(lambda ciclista: vars(ciclista), ciclistas))
    print('Se consultaron los ciclistas 👍')
    return ciclistas_como_diccionarios

@eel.expose
def barra_de_busqueda_general_ciclistas(sentencia_de_busqueda):
    ciclistas = CiclistaDAO.buscar_en_todos_los_campos(conexion, sentencia_de_busqueda)
    ciclistas_como_diccionarios = list(map(lambda ciclista: vars(ciclista), ciclistas))
    print(f'Se realizó la búsqueda: "{sentencia_de_busqueda}"')
    return ciclistas_como_diccionarios

@eel.expose
def consultar_ciclista(numero_de_ciclista):
    ciclista = CiclistaDAO.consultar_ciclista(conexion, numero_de_ciclista)
    ciclistas_como_diccionarios = vars(ciclista)
    print(f'Se consultó al ciclista {numero_de_ciclista}')
    return ciclistas_como_diccionarios

@eel.expose
def eliminar_ciclista(numero_de_ciclista):
    CiclistaDAO.eliminar_ciclista_por_id(conexion, numero_de_ciclista)
    print(f'Se eliminó al ciclista {numero_de_ciclista}')

@eel.expose
def ciclista_actualizar_nacionalidad(numero_de_ciclista, nuevo_pais):
    CiclistaDAO.actualizar_pais(conexion, numero_de_ciclista, nuevo_pais)
    print(f'Se actualizó la nacionalidad del ciclista {numero_de_ciclista}')

@eel.expose
def crear_ciclista(*args):
    nombre, apellido, link_fotografia, identificacion, pais, fechaDeNacimiento, nombre_equipo, rankingUCI = args
    id_equipo = EquipoDAO.id_de_equipo_por_nombre(conexion, nombre_equipo)
    # imagen_en_bytes = imagen_en_base_64.encode('utf-8')
    
    if id_equipo == None:
        return('No conozco ese equipo 😳😳👈')
    try:
        ciclista = Ciclista(nombre=nombre, apellido=apellido,fotografia=link_fotografia, num_identificacion=identificacion,pais=pais,fecha_nacimiento=fechaDeNacimiento, num_equipo=id_equipo, ranking_UCI=rankingUCI)
    except ValueError as error:
        print(error)
    

    CiclistaDAO.crear_ciclista(conexion, ciclista)
    print(f'Se creo el ciclista {args[0]}')
def ciclista_actualizar_ranking(numero_de_ciclista, nuevo_ranking):
    CiclistaDAO.actualizar_ranking(conexion, numero_de_ciclista, nuevo_ranking)
    print(f'Se actualizó el ranking del ciclista {numero_de_ciclista}')



#Inicializar conexión js/python
eel.init('client')
eel.start('home.html')