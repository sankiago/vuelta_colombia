from   logica.init_db        import conexion_a_la_db, eliminar_tablas, crear_tablas
from   logica                import *
import eel

#Inicializar base de datos
conexion = conexion_a_la_db('base_de_datos_vc.db')
crear_tablas(conexion)

#Exponiendo funciones a js
@eel.expose
def consultar_todos_los_ciclistas():
    ciclistas = CiclistaDAO.consultar_info_vigente(conexion)
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
    ciclista = CiclistaDAO.consultar_info_vigente_ciclista(conexion, numero_de_ciclista)
    ciclistas_como_diccionarios = vars(ciclista)
    print(f'Se consultó al ciclista {numero_de_ciclista}')
    return ciclistas_como_diccionarios

#Inicializar conexión js/python
eel.init('client')
eel.start('home.html')