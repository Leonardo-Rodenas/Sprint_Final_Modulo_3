import random
import string

def crear_contrasena(largo):
    """Función que crea contraseñas aleatorias de mayúsculas. minúsculas y dígitos"""
    caracteres_disponibles = string.ascii_letters + string.digits
    retorno = ""
    for i in range(largo):
        retorno += caracteres_disponibles[random.randint(0,len(caracteres_disponibles)-1)]
    return retorno

def remover_tildes(string_nombre):
    """Función que remueve tildes de los nombres, si es que los tienen"""
    retorno = string_nombre
    retorno = retorno.replace("á", "a")
    retorno = retorno.replace("é", "e")
    retorno = retorno.replace("í", "i")
    retorno = retorno.replace("ó", "o")
    retorno = retorno.replace("ú", "u")
    return retorno

def crear_nombre_usuario(nombre, edad):
    """Función que crea nombre de usuario para la cuenta, tomando las 4 primeras letras del primer nombre, el apellido sin las últimas 3 letras y la edad"""
    nombre_usuario = remover_tildes(nombre[0:4].lower()) + remover_tildes(nombre[nombre.index(" ")+1:-3].lower().replace(" ","_")) + str(edad)
    return nombre_usuario

# - Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
def generar_cuenta(pacientes):
    """Función que crea una cuenta con id_acceso = nombre de usuario y la contraseña (usando las funciones antes creadas)"""
    retorno = []
    for persona in pacientes:
        elemento = {
            "id_acceso": crear_nombre_usuario(persona["nombre"], persona["edad"]),
            # - Asigne una contraseña para cada cuenta. La contraseña debe ser creada con random y debe cumplir con lo siguientes: mayúsculas, minúsculas y números.
            "password": crear_contrasena(10)
        }
        retorno.append(elemento)
    return retorno

def crear_telefono(pacientes):
    """Función que pide el ingreso de teléfono por cada cuenta, verifica al menos 8 dígitos y pregunta otra vez al mismo ususario en caso de no tener el fono correcto"""
    for paciente in pacientes:
        # - El programa no terminará de preguntar por los números hasta que todas las organizaciones tengan un número de contacto asignado.
        while True:
            telefono = input(paciente["nombre"] + ", ingrese su teléfono por favor: ")
            # - El programa debe verificar que el número telefónico tenga 8 dígitos numéricos.
            if len(telefono) >= 8 and telefono.isdigit():
                paciente["telefono"] = telefono
                break
            else:
                print("Su teléfono debe tener como mínimo 8 dígitos")
                
    return pacientes
