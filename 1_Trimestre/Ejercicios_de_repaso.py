"""EJERCICIO 1. 
Dado el numero entero x=103 y el numero decimal y= 7.5, realiza las siguientes operaciones combinadas en un solo calculo y determina el resultado:
"""
x, y = 103 , 7.5 #definicion de variables
print (f"x = {x}({type(x)})\t\ty = {y}({type(y)})") #comprobacion de formato de dato

#1. Divide x entre y.
print (x/y)

#2. Calcula el resto de la division entera del resultado del paso anterior entre 5.
print ((x/y) % 5)

#3. Eleva ese resto al cuadrado.
print (((x/y) % 5)**2)



"""EJERCICIO 2. 
Crea una cadena que combine las siguientes piezas:
"""
#declaracion de variables:
cadena , especial , cadena2 = "Python" , "@" , "Framework"

#1. La primera letra de la cadena "Python". (lo hago a traves de los indices) 
print(len(cadena[0]))

#2. Tres veces el carácter especial "@".
print(especial *3)

#3. El último carácter de la cadena "Framework".
print(cadena2 [len(8)])

#4. Concatenar todo y convertir el resultado en mayúsculas.
resultado = cadena[0] + especial*3 + cadena2 [len(cadena2)-1].upper()
print(f"El resultado de lo solicitado en los cuatro puntos es: {resultado}")




"""EJERCICIO 3. 
Dada la lista q = [2, "a", [3.5 , 4], "Python"], accede al número 4 y eleva su valor al cuadrado:
"""
q = [2, "a", [3.5 , 4], "Python"]
print(f"El cuadrado del valor 4 existente en la lista q = {q} se accede mendiante la instrucción q[2][1]**2 que es igual a: {q[2][1]**2}")


"""EJERCICIO 4. 
Crea un diccionario que tenga las siguientes claves y valores:
"""
#1. Clave "a", valor: el cuadrado del número 5.
#2. Clave "b", valor: una lista con los números del 1 al 3.
#3. Clave "c", valor: una tupla que contenga los caracteres "x" y "y" concatenados.

#creamos el diccionario con las llaves {} y definimos las claves, con la estructura clave valor:
d = {
    "a": 5**2,
    "b": [1 ,2 , 3], #los corchetes sirven en un diccionario para hacer las listas
    "c": ("x" + "y" , ) #los parentesis son para en los diccionarios hacer las tuplas
}
#4. Obtén el largo del valor asociado a la clave "b".
print(f"Sea el diccionario d = {d} la longitud de la clave 'b' es: {len(d['b'])} elementos")



"""EJERCICIO 5. 
Convierte la cadena "1234" en un número entero, súmale 6, conviértelo nuevamente a cadena y repítelo 3 veces:
"""
#creamos la variable
cadena = "1234"
print(f"La cadena '{cadena}' es de tipo: {type(cadena)}")

#la paso a entero:
cadena = int(cadena)
print(f"La cadena '{cadena}' es de tipo: {type(cadena)}") #compruebo el cambio

#le sumo 6, lo convierto a string de nuevo y lo repito 3 veces:
cadena = str(int("1234") + 6)*3
print(f"La cadena= 1234 al aplicar la operacion: str(int("cadena") + 6)*3 = {cadena} y su formato es de tipo: {type(cadena)}") #compruebo el cambio



"""EJERCICIO 6. 
Dada la lista ["1", 2, 3.0, True], realiza las siguientes acciones:
"""
#creo la variable
lista = ["1", 2, 3.0, True]

#1. Convierte el primer elemento entero.
int(lista[0])

#2. Suma todos los elementos de la lista.
lista[0]= int(lista[0]) #casteo y actualizo el valor de la lista
print(f"Sea la lista: {lista} la suma es {sum(lista)}") #nos tiene que dar 7 porque true vale 1.



"""EJERCICIO 7. 
Evalúa si las siguientes condiciones se cumplen:
"""
condicion1 , condicion2 = 8+3 > 2*6 , 20//3 == 25 % 5
#1. La suma de los números 8 y 3 es mayor que el producto de 2 por 6.
print(f"¿La suma de los numeros 8 y 3 es mayor que el producto de 2 por 6?: {8+3 > 2*6}") #no se cumple la condicion

#2. La división entera de 20 entre 3 es igual al resto de 25 dividido por 5.
print(f"¿La división entera de 20 entre 3 es igual al resto de 25 dividido por 5?: {20//3 == 25 % 5 }") #no se cumple la condicion

#podriamos poner el r+esultado asi:
print(f"¿Condicion1 (8+3 > 2*6 es {condicion1}) y la condicion2 (20//3 == 25 % 5 es {condicion2}) se cumplen?: {condicion1 and condicion2}")



"""EJERCICIO 8. 
Crea una tupla con 4 elementos, y evalúa si el primer elemento es diferente del último:
"""
#creo una tupla con elementos:
t = (1 , "a" , 2 , 1)
print(f"Sea la tupla t= {t}, ¿Es el primer elemento {t[0]} distinto del último elemento ({t[len(t)-1]})?: {t[0]!= t [len(t)-1]}")
print(t[0]!= t [len(t)-1])
