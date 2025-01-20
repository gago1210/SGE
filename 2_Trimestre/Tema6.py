#FUNCIONES

"""Sintaxis:
def <<nombre_funcion>>(<<parametro/s>>)
|   '''<<documentacion_funcion>>'''
|   <<cuerpo_funcion>>
|   return <<obj_a_devolver>>
"""
def saludar(n):
    '''
    OBJETIVO: saludar recibiendo un nombre
    PARAMETROS: 
        + n[str]: nombre que recibe como parametro
    VARIABLES:
        + o[str]:saludo con el nombre
    RETURN: 
        + o[str]:
    '''

    o = f"Hola, {n}!"
    return o 

print(saludar("Juan"))
print(saludar.__doc__) #esto es lo mismo que  print(help(saludar))


def suma(a = 0 , b = 0):
    return a + b
print(suma() , suma(3 , 2))


def saludar():
    def preguntar():
        x = input("Nombre: ")
        return x
    n = preguntar()
    o = f"¡Hola, {n}!"
    return o
print(saludar())


def operacion(a , b , op = "resta"):
    def suma(a , b):
        return a + b
    def resta(a , b):
        return a - b
    if op == 'resta':
        return resta(a , b)
    else:
        return suma(a , b)
print(operacion(5 , 4, "suma"))


saludar = lambda: "hola"
print(saludar())

resta = lambda a , b: a + b
print(suma(3 , 2))

resta = lambda a = 0, b = 0: a - b
print(resta(3))


def suma(a , b):
    return lambda: a + b
print(suma(2 , 3)())

def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorar_c():
        print("codigo a ejecutar antes de la funcion")
        funcion_a_decorar_b()
        print("codigo a ejecutar despues de la funcion")
    return funcion_decorador_c

@funcion_decorador_a
def saludar():
    print("Hola")
saludar()
