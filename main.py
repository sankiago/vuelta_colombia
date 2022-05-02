from logica.init_db        import conexion_a_la_db, eliminar_tablas, crear_tablas
from presentacion.menu     import mostrar_menu

#Inicializar base de datos
conexion = conexion_a_la_db('base_de_datos_vc.db')

crear_tablas(conexion)

mostrar_menu(conexion)



