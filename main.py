from   logica.init_db        import conexion_a_la_db, eliminar_tablas, crear_tablas
from   logica                import *
import eel

#Inicializar base de datos
conexion = conexion_a_la_db('base_de_datos_vc.db')
crear_tablas(conexion)

#Exponiendo funciones a js
EquipoDAO
CiclistaDAO
EtapaDAO
Resultado_DAO

#Inicializar conexión js/python
eel.init('client')
eel.start('home.html')







