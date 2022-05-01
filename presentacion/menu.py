from   time import sleep
import os
banner = """
  _   __         ____         _____     __           __   _     
 | | / /_ _____ / / /____ _  / ___/__  / /__  __ _  / /  (_)__ _
 | |/ / // / -_) / __/ _ `/ / /__/ _ \/ / _ \/  ' \/ _ \/ / _ `/
 |___/\_,_/\__/_/\__/\_,_/  \___/\___/_/\___/_/_/_/_.__/_/\_,_/
"""
vuelta_colombia_2 = """
 __   __        _ _           ___     _           _    _      
 \ \ / /  _ ___| | |_ __ _   / __|___| |___ _ __ | |__(_)__ _ 
  \ V / || / -_) |  _/ _` | | (__/ _ \ / _ \ '  \| '_ \ / _` |
   \_/ \_,_\___|_|\__\__,_|  \___\___/_\___/_|_|_|_.__/_\__,_|
"""

opciones = {
    1 : '   1. Crear nuevo equipo\n',
    2 : '   2. Consultar información de equipo por número de identificación\n',
    3 : '   3. Cambiar sede central de equipo\n',
}

menu_text = """
Bienvenido a vuelta colombia ¿Qué desea hacer en estos momentos?

Digite el número de la opción en la que esta interesado
Gestión de equipos:
"""

os.clear()
print(banner)
print()
print('')
print('Gestión de equipos')
print(' ')