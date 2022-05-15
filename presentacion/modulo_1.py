from logica          import EquipoDAO
from modelos         import Equipo
from terminaltables  import AsciiTable

def crear_equipo_user(conexion):
    '''
    Funcion que crea el equipo
    Recibe un ojeto conexion
    '''
    print('Ingrese los datos del nuevo equipo.')
    nombre                 = input('nombre: ')
    pais                   = input('pais: ')
    director               = input('director: ')
    marca_bicicleta        = input('marca de bicicleta: ')
    marca_ciclocomputador  = input('marca_ciclocomputador: ')
    direccion_sede_central = input('dirección de la sede central: ')
    telefono               = input('número de telefono: ')
    correo_electronico     = input('dirección de correo electrónico: ')

    equipo = Equipo(nombre=nombre, pais=pais, director=director, marca_bicicleta=marca_bicicleta, marca_ciclocomputador=marca_ciclocomputador, direccion_sede_central =direccion_sede_central, telefono=telefono, correo_electronico=correo_electronico)
    EquipoDAO.crear_equipo(conexion, equipo)
    print(f'El equipo {nombre} se ha creado con éxito')

def consultar_equipo_por_id_user(conexion):
    '''
    Funcion que encuentra un equipo por el id del equipo
    Recibe el objeto conexion
    '''
    id_equipo          = input('Ingrese el número del equipo: ')
    equipo = EquipoDAO.consultar_equipo_por_id(conexion, id_equipo)
    if equipo == None:
        print(f'No se ha encontrado el equipo número {id_equipo}')
    else:
        cuerpo_de_la_tabla      = [equipo.convertir_a_lista()]
        encabezados_de_la_tabla = [['Número de equipo', 'Nombre', 'País', 'Director', 'Marca de bicicleta', 'Marca de ciclocomputador','Dirección de sede central', 'Teléfono', 'Correo electrónico']]
        datos_de_la_tabla       = encabezados_de_la_tabla + cuerpo_de_la_tabla
        tabla_equipo            = AsciiTable(datos_de_la_tabla)
        tabla_equipo.title      = ' Consulta de equipos '
        print(tabla_equipo.table)

def cambiar_sede_equipo_user(conexion):
    '''
    Funcion que se encarga de cambiar la sede en la que se inscribio el equipo
    Recibe como objeto conexion
    '''
    id_equipo       = input('Ingrese el número del equipo: ')
    nuevo_pais      = input('Ingrese el nuevo país de sede: ')
    nueva_direccion = input('Ingrese el la dirección de la nueva sede del equipo: ')
    EquipoDAO.cambiar_sede_equipo(conexion,id_equipo, nuevo_pais, nueva_direccion)
    print(f'La información de la sede del equipo {id_equipo} ha sido modificada.')
