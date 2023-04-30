from sprint_funciones import crear_telefono, generar_cuenta 

# - Lista de nombres y atributos del usuario
pacientes = [
    {
        "nombre": "María Gonzalez",
        "edad": 42,
        "direccion": "Av. 20 de Septiembre #342, Quillota",
    },
    {
        "nombre": "Arturo Lopez",
        "edad": 28,
        "direccion": "José Manuel Infante 805, Providencia, Santiago. ",
    },
    {
        "nombre": "Juan Ramírez",
        "edad": 36,
        "direccion": "Bulnes #82, Limache",
    },
    {
        "nombre": "Sofía Gomez",
        "edad": 23,
        "direccion": "Villa Los Perales, Pasaje J #46, La Calera",
    },
    {
        "nombre": "Tony Montana",
        "edad": 33,
        "direccion": "Hello my little friend #1983, Viña del Mar ",
    },
    {
        "nombre": "Mario Fernandez",
        "edad": 66,
        "direccion": "Bulnes #82, Quillota",
    },
    {
        "nombre": "Dwayne Jhonson",
        "edad": 50,
        "direccion": "Calle La Roca #72, Santiago",
    },
    {
        "nombre": "Florinda Meza",
        "edad": 70,
        "direccion": "Villa Mexico, pasaje La Vecindad, departamento #14, Quillota",
    },
    {
        "nombre": "María Nieves",
        "edad": 72,
        "direccion": "Villa Mexico, pasaje La Vecindad, departamento #72, Quillota",
    },
    {
        "nombre": "Roberto Gómez",
        "edad": 85,
        "direccion": "Villa Mexico, pasaje La Vecindad, departamento #8, Quillota",
    }
]

# - Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu aplicación.
print(pacientes)
print()

# - Cada cuenta debe guardarse en una nueva variable con su respectiva contraseña.
accesos = generar_cuenta(pacientes)
print(accesos)
print()

# - Por cada cuenta debe pedir un número telefónico para contactarse.
# - Se debe guardar como un string.
telefonos = crear_telefono(pacientes)
print()
print(pacientes)