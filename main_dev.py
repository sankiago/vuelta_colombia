from logica.init_db        import conexion_a_la_db, eliminar_tablas, crear_tablas
from presentacion.menu     import mostrar_menu
from presentacion.modulo_2 import consultar_info_vigente_ciclista_user

#Inicializar base de datos
conexion = conexion_a_la_db('test.db')

# crear_tablas(conexion)
mostrar_menu(conexion)





