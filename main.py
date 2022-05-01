from logica.init_db        import conexion_a_la_db, eliminar_tablas, crear_tablas
from logica.modulo_1       import crear_equipo
from presentacion.modulo_1 import consultar_equipo_por_id_user, crear_equipo_user,cambiar_sede_equipo_user
from logica.modulo_2       import crear_ciclista
from presentacion.modulo_2 import consultar_info_vigente_user, crear_ciclista_user, cambiar_ranking_UIC_user
from presentacion.modulo_3 import crear_etapa_user, actualizar_info_ciclista_user

#Inicializar base de datos
conexion = conexion_a_la_db()
#   Eliminar esta línea cuando se hallan acabado las pruebas
eliminar_tablas(conexion)
crear_tablas(conexion)

mi_equipo = ['rayos makuines','tauramena', 'santiaguinho', 'nosexd', 'yo', 'aja', '234', 'dlopezda@unal.edu.co']
crear_equipo(conexion, mi_equipo)
mi_ciclista = ['1118534262','santiago','lopez','1061960400.0','polombia','1','13']
crear_ciclista(conexion, mi_ciclista)
crear_etapa_user(conexion)
actualizar_info_ciclista_user(conexion)


