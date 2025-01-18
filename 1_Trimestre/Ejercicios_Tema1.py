"""Crear una variable (u) que guarde el valor ocho en formarto de caracter. Multiplicarlo posteriormente
    por tres unidades enteras. Y su resultado pasarlo a un valor numérico de tipo entero."""

u = int ("8"*3)
print (u)



"""Crear un código resiliente, de tal manera que el programa pida al usuario introducir el año de nacimiento 
    y que él mismo calcule la edad que tiene esa persona."""

a = input ("Año de nacimiento: ")
edad = 2024 - int (a)
print (edad, type (edad))

#podemos hacer esto tambien más sencillo:
a = 2024 - int (input ("Año de nacimiento: "))
print ("Tienes una edad de " , a, "años")

# o esta, mas sencilla aún:
print ("Tienes una edad de ", 2024-int (input ("Año de nacimiento: ")), "años")



"""Crear un código resiliente, de tal manera que el programa pida el precio del productom que ha de ser introducido por
    teclado, de un artículo (los precios pueden ser enteros o no)."""   

p = float (input ("Precio: "))
print (p, type (p))



"""Continuando con el ejercicio anterior, se pide que el precio sea truncado y permita trabajar en formato numérico."""
p = int (float (input ("Precio: ")))
print (p, type (p))
#lo que hace aqui el utilizar el valor int como funcion  de cohercion o casteo, previo a float, lo que hace es truncarlo.
# si hubieramos puesto p = float (int (input ("Precio: "))), si metemos un numero entero, no hay problema, pero si pasamos
# un valor de formato decimal, nos lo conoce como tipo string y nos da error. De la otra manera, nos transforma el float
#espera ese valor decimal, espera el punto del 3.0.



"""Crear un código resiliente de tal manera que el programa pida al usuario introducir el año de nacimiento y que el mismo calcule la edad que 
    tiene esa persona. """

b = input ("Año de nacimiento: ")
edad = 2024 -int (b)
print (edad, type (edad))
    #otra forma de ponerlo seria:
print ("Tienes una edad de", 2024 - int (input ("Año de nacimiento: "), "años"))



"""Crear un codigo resiliente, de tal manera que el programa pida el precio del producto que ha de ser introducido por teclado, de un articulo.
    los precios pueden ser enteros o no """
p = float(input("Precio: "))
print (p, type(p))



"""Continuando con el ejercicio anterior, se pide que el precio sea truncado y permita trabajar en formato numerico"""
p = int (float(input ("Precio: ")))
print (p, type(p))