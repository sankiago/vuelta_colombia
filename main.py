from init_db  import conexion_a_la_db, eliminar_tablas, crear_tablas
from modulo_1 import crear_equipo    , consultar_equipo_por_id

#Inicializar base de datos
conexion = conexion_a_la_db()
# Eliminar esta línea cuando se hallan acabado las pruebas
eliminar_tablas(conexion)
crear_tablas(conexion)
mi_equipo = ['tauramena', 'santiaguinho', 'nosexd', 'yo', 'aja', '322', 'asdasd']
crear_equipo(conexion, mi_equipo)
consulta_de_mi_equipo = consultar_equipo_por_id(conexion, 1)
print(consulta_de_mi_equipo)
