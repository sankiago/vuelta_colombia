from logica.init_db  import conexion_a_la_db, eliminar_tablas, crear_tablas
from logica.modulo_1 import crear_equipo
from presentacion.modulo_1 import consultar_equipo_por_id_user, crear_equipo_user

#Inicializar base de datos
conexion = conexion_a_la_db()
#   Eliminar esta línea cuando se hallan acabado las pruebas
eliminar_tablas(conexion)
crear_tablas(conexion)

crear_equipo_user(conexion)
consultar_equipo_por_id_user(conexion)
consultar_equipo_por_id_user(conexion)