from logica.init_db  import conexion_a_la_db, eliminar_tablas, crear_tablas
from logica.modulo_1 import crear_equipo
<<<<<<< HEAD
from presentacion.modulo_1 import consultar_equipo_por_id_user, crear_equipo_user,cambiar_sede_equipo_user
=======

from presentacion.modulo_1 import consultar_equipo_por_id_user, crear_equipo_user
>>>>>>> 11ebfb6a904ec4de2d6f90228f7103f4f6a4cc43

from logica.modulo_3
from presentacion.modulo_3

#Inicializar base de datos
conexion = conexion_a_la_db()
#   Eliminar esta línea cuando se hallan acabado las pruebas
eliminar_tablas(conexion)
crear_tablas(conexion)

<<<<<<< HEAD
mi_equipo = ['rayos makuines','tauramena', 'santiaguinho', 'nosexd', 'yo', 'aja', '234', 'dlopezda@unal.edu.co']
crear_equipo(conexion, mi_equipo)
cambiar_sede_equipo_user(conexion)
=======

crear_equipo_user(conexion)
consultar_equipo_por_id_user(conexion)
consultar_equipo_por_id_user(conexion)
>>>>>>> 11ebfb6a904ec4de2d6f90228f7103f4f6a4cc43
