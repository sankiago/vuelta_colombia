from pick import pick
from presentacion.modulo_1 import crear_equipo_user,   consultar_equipo_por_id_user, cambiar_sede_equipo_user
from presentacion.modulo_2 import crear_ciclista_user, cambiar_ranking_UIC_user,     consultar_info_vigente_user, consultar_info_vigente_ciclista_user
from presentacion.modulo_3 import crear_etapa_user,    actualizar_info_ciclista_user
from presentacion.modulo_4 import consulta_etapa_user, consulta_general_user
import os
from time import sleep

banner = """  _   __         ____         _____     __           __   _     
 | | / /_ _____ / / /____ _  / ___/__  / /__  __ _  / /  (_)__ _
 | |/ / // / -_) / __/ _ `/ / /__/ _ \/ / _ \/  ' \/ _ \/ / _ `/
 |___/\_,_/\__/_/\__/\_,_/  \___/\___/_/\___/_/_/_/_.__/_/\_,_/

 
----------------------------------------------------------------
"""

def limpiar_pantalla():
    '''Como su nombre lo dice, esta función se encarga de limpiar la pantalla, es decir, 
    borrar los elementos que se encuentran en la misma'''
    os.system('cls' if os.name == 'nt' else 'clear')

limpiar_pantalla()

modulos = {
    'opciones' : ['Gestionar equipos','Gestionar ciclistas','Cargar resultados de una etapa','Consultar clasificación general o por etapas', 'Salir'],
    1 : {
        'opciones':['Crear nuevo equipo', 'Consultar equipo', 'Cambiar sede central de un equipo', 'Regresar al menú principal'],
        1 : crear_equipo_user,
        2 : consultar_equipo_por_id_user,
        3 : cambiar_sede_equipo_user,
    },
    2:{
        'opciones': ['Crear nuevo ciclista', 'Actualizar ranking UIC de un ciclista', 'Ver ciclistas', 'Consultar ciclista' ,'Regresar al menú principal'],
        1 : crear_ciclista_user,
        2 : cambiar_ranking_UIC_user,
        3 : consultar_info_vigente_user,
        4 : consultar_info_vigente_ciclista_user
    },
    3:{
        'opciones': ['Cargar tiempo de la etapa un ciclista', 'Actualizar tiempo de la etapa de un ciclista','Regresar al menú principal'],
        1: crear_etapa_user,
        2: actualizar_info_ciclista_user,
    },
    4:{
        'opciones': ['Consultar clasificación de una etapa', 'Consultar clasificación general','Regresar al menú principal'],
        1: consulta_etapa_user,
        2: consulta_general_user, 
    }
}

def mostrar_menu(conexion):
    '''Esta funcion contiene los elementos con los que el usuario interactuara, 
    lo que se mostrara en la terminal'''
    titulo_menu                    = banner + '\n¿Qué desea hacer el día de hoy?'
    modulo_seleccionado            = pick(modulos['opciones'], titulo_menu)[1] + 1
    if modulo_seleccionado == 5:
        quit()
    opcion_de_funcion_seleccionada = pick(modulos[modulo_seleccionado]['opciones'], modulos['opciones'][modulo_seleccionado - 1])[1] + 1
    
    selecciono_menu_principal = opcion_de_funcion_seleccionada == len(modulos[modulo_seleccionado]['opciones'])
    
    if not selecciono_menu_principal:
        funcion_seleccionada           = modulos[modulo_seleccionado][opcion_de_funcion_seleccionada] 
        ejecutar_funcion_de_nuevo = True
        while ejecutar_funcion_de_nuevo:
            se_ha_completado_la_funcion_correctamente = False
            while not se_ha_completado_la_funcion_correctamente:
                try:
                    funcion_seleccionada(conexion)
                    se_ha_completado_la_funcion_correctamente = True
                    input('\nPresione enter para continuar')
                except ValueError as error:
                    print(f'\n{error}\n\n')

            descripcion_de_la_funcion_seleccionada = modulos[modulo_seleccionado]['opciones'][opcion_de_funcion_seleccionada - 1]
            pregunta  = f'¿Desea {descripcion_de_la_funcion_seleccionada.lower()} otra vez?'
            opciones  = ['Sí', 'No']
            respuesta = not bool(pick(opciones, pregunta)[1])
            limpiar_pantalla()
            ejecutar_funcion_de_nuevo = respuesta
    mostrar_menu(conexion)