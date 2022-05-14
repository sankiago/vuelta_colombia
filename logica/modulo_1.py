# Módulo 1: Módulo de gestión de equipos inscritos y afiliados
# Importando librerias necesarias para enviar el correo electrónico de los inscritos
import smtplib, ssl
from   email.message import EmailMessage
import re
from modelos import Equipo, equipo

def crear_equipo(conexion, equipo):
  """
  Función creación de equipo.
  Recibe un objeto Connection (conexion).
  Recibe un objeto de la clase Equipo
  """
  if type(equipo) != Equipo:
    raise ValueError('No se ingreso un equipo')
  cursor              = conexion.cursor()
  sentencia_insercion = 'INSERT INTO equipos(nombre, pais_sede, director, marca_bicicleta, marca_ciclocomputador, direccion_sede_central, telefono, correo_electronico) VALUES(?,?,?,?,?,?,?,?)'
  cursor.execute(sentencia_insercion, equipo.convertir_a_lista())
  conexion.commit()
  enviar_correo_verificacion(director=equipo.director, equipo=equipo.nombre, correo=equipo.correo_electronico)

def consultar_equipo_por_id(conexion, id_equipo):
  """
  Función consulta por número de equipo.
  Recibe un objeto Connection (conexion).
  Recibe el número de equipo a consultar (id_equipo).
  """
  cursor             = conexion.cursor()
  sentencia_consulta = f'SELECT * FROM equipos WHERE num_equipo = {id_equipo}'
  respuesta_consulta = cursor.execute(sentencia_consulta).fetchall()
  if len(respuesta_consulta) == 0:
    equipo_consultado = []
  else:
    equipo_consultado  = Equipo(lista_de_informacion=respuesta_consulta[0])

  return equipo_consultado

def cambiar_sede_equipo(conexion, id_equipo, nuevo_pais, nueva_direccion):
  """
  Función cambio de sede central de un equipo.
  Recibe un objeto Connection (conexion).
  Recibe el número del equipo a modificar (id_equipo).
  Recibe la nueva dirección de sede.
  """
  cursor                  = conexion.cursor()
  sentencia_actualizacion = f'UPDATE equipos SET pais_sede = "{nuevo_pais}", direccion_sede_central = "{nueva_direccion}" WHERE num_equipo = {id_equipo}'
  cursor.execute(sentencia_actualizacion)
  conexion.commit()

import smtplib, ssl
from email.message import EmailMessage



def enviar_correo_verificacion(**destinatario):
  """
  Función que envia un correo de verifcación que dice:
  Estimad@ {nombre} {apellido} su inscripcion a La Vuelta Colombia ha sido finalizada con exito.
  Gracias por participar
  Recibe como parámetro de la función los siguientes parámetros nombrados
  director, equipo, correo (**destinatario)
  """

  mensaje  = f"""Estimad@ {destinatario['director']} la inscripcion del equipo {destinatario['equipo']} a La Vuelta Colombia ha sido finalizada con exito.
Gracias por participar"""

  # email que creamos para enviar los correos xd
  remitente              = 'trabajopooxd@gmail.com'
  contrasena_remitente   = 'trabajito poo'
  asunto                 = 'Confirmación inscripción a La Vuelta Colombia.'

  # Se crea un objeto de la clase EmailMessage el cual va a ser enviado por el servidor smtp como mensaje
  correo_electronico            = EmailMessage()
  # Asignando el contenido, asunto, remitente y destinatario al objeto correo_electronico
  correo_electronico.set_content(mensaje)
  correo_electronico['Subject'] = asunto
  correo_electronico['From']    = remitente
  correo_electronico['To']      = destinatario['correo']

  # Variables para ajustes del servidor
  puerto = 465  # For SSL
  servidor_smtp = "smtp.gmail.com"
  contexto = ssl.create_default_context()

  # Creando el servidor y enviando el correo
  with smtplib.SMTP_SSL(servidor_smtp, puerto, context=contexto) as servidor:
        # Iniciando sesión en el servidor
        servidor.login(remitente, contrasena_remitente)
        #Enviando el correo electronico
        servidor.send_message(correo_electronico, from_addr=remitente, to_addrs=destinatario['correo'])
        print(f"Se ha enviado un correo de verificación a {destinatario['director']} {destinatario['correo']}")