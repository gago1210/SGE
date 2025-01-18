#1/10/24
"""Ejercicio 1: Escribir un programa que muestre por pantalla la cadena '¡Hola Mundo!' """
print ("¡Hola Mundo!")

"""Ejercicio 2: Escribir un programa que almacene la cadena '¡Hola Mundo!' en una variable y luego muestre por pantalla el
    contenido de la variable. """
x = "¡Hola Mundo!"
print (x)

"""Ejercicio 3: Escribir un programa que pregunte el nombre del usuario en la consola despues de que el usuario lo
    introduzca, lo muestre por pantallla la cadena '¡Hola <nombre>!, donde <nombre> es el nombre que el usuario 
    haya introducido."""
l = input ("Nombre:")
print (" Hola" + l + "!")


"""Ejercicio 4: Escribir un programa que muestre por pantalla el resultado de la siguiente operacion aritmética 
    ((3+2)/(2*5))**2"""
s = ((3+2) / (2*5))**2
print ("El resultado de ((3+2) / (2*5))**2 es ", s)


"""Ejercicio 5: Escribir un programa que pregunte al usuario por el numero de horas(h) trabajadas y el coste (c) por hora.
    Después debe mostrar por pantalla la paga que le corresponde."""
h, c = float(input ("Horas trabajadas: ")) , float(input ("Precio hora: "))
print ("Si has trabajado" ,h, "horas, y el precio por hora es" , c, "euros, has ganado", c*h, "euros")

#8/10/24
"""Ejercicio 6: Escribir un programa que lea un entero positivo, n, introducido por el usuario y despues muestre en 
    pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada
    de la siguiente forma: suma= (n(n+1))/2."""
e = int (float (input("Entero positivo: ")))
suma = int (0.5 * e * ( e+1))
print(" La suma de enteros, comprendida desde 1 a " , e, "es:" , suma, ".")


"""Ejercicio 7: Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el indice de masa 
    corporal y lo almacene en una variable, y muestre por pantalla la frase 'Tu indice de masa corporal es <imc> donde 
    <imc> es el indice de masa corporal calculado redondeado con dos decimales."""
p , a = round(float (input ("Peso en kg: ")),2) , round (float (input ("Altura en m: ")),2)
imc = round (p / a **2 , 2)
print ("Tu indice de masa corporal es: ", imc)


"""Ejercicio 8: Escribir un programa que pida al usuario dos numeros enteros y muestre por pantalla la <n> entre <m> de 
    un cociente <c> y un resto <r> donde <n> y <m> son los numeros introducidos por el usuario, y <c> y <r> son el 
    cociente y el resto de la division entera respectivamente."""
n, m = int (float (input ("n: "))) , int(float (input ("m")))
c, r = n // m, n % m
print (n, "entre" , m, "da un cociente" , c, " y un resto", r)


"""Ejercicio 9: Escribir un programa que pregunte al usuario una cantidad (i) a invertir, el interés anual (y) y el número 
    de años (z), y muestre por pantalla el capital obtenido en la inversión (k)"""
i, y, z = 1000 , 2.66 , 1 , round (float(input("capital a invertir: ")),2), round (float(input("interés %: ")),2) , round (int(input("numero de años:  ")))
k = i * (1/100) * y * z #o lo que es lo mismo: k = i * 0.01 * y * z, esto es el rendimiento de la inversión.
print ("con un capital de ", i , "euros, y un interés del: " , y , "% y" , z , " años, obtenemos un rendimiento de" , k , "euros")


"""Ejercicio 10: Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo 
    y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas 
    que saldrán en cada paquete a demanda. Cada payaso pesa 112 gramos y cada muñeca 75 gramos. Escribir un programa que 
    lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado."""
payasos, muñecas, pesopayaso, pesomuñeca = int(float(input("Numero de payasos: "))) , int(float(input("Numero de muñecas: "))), 0.112, .075 
pesototal = round (payasos *pesopayaso + muñecas * pesomuñeca, 3) #peso total del paquete que será enviado 
print ("Se ha pedido un total de ", payasos , "payasos y ", muñecas ,"muñecas, por lo que el envío es de ", pesototal , "kilos (las muñecas y los payasos pesan) ", pesomuñeca, ",", pesopayaso, "kilos" )


"""Ejercicio 11: Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros
    debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros.
    Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el
    usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer
    años. Redondear cada cantidad a dos decimales."""
capitalinicial , interes = round(float(input("Cantidad de dinero (euros): ")),2) , 0.04
print("En el año 0, con un capital de " , capitalinicial, "euros a un interés del" , interes * 100, "%, obtengo un rendimiento de 0 euros" )
rendimiento1año = round (capitalinicial * interes , 2) 
print("En el año 1, con un capital de " , capitalinicial, "euros a un interés del" , interes * 100, "%, obtengo un rendimiento de", rendimiento1año, "euros" )
rendimiento2año = round ((capitalinicial + rendimiento1año) * interes , 2)
print("En el año 2, con un capital de " , capitalinicial + rendimiento1año, "euros a un interés del" , interes * 100, "%, obtengo un rendimiento de", rendimiento2año, "euros" )
rendimiento3año = round((capitalinicial + rendimiento2año) * interes , 2)
print("En el año 3, con un capital de " , capitalinicial + rendimiento2año, "euros a un interés del" , interes * 100, "%, obtengo un rendimiento de", rendimiento3año, "euros" )
print("El capital obtenido es: " , capitalinicial + rendimiento1año + rendimiento2año + rendimiento3año , "euros")


"""Ejercicio 12: Una panadería vende barras de pan a 3.49 euros cada una. El pan que no es del día, tiene un descuento del 60%.
    Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar
    el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total."""
#al ser un descuento del 60%, lo que yo pago de la barra es el 40% restante, nos quedamos con ello que es mas facil trabajar asi
numerobarras , precio ,  preciodescuento = int(float(input("Numero de barras no son frescas: " ))) , 3.49 , 0.4
print ("El precio de la barra de pan es" , precio, "euros; el descuento aplicado es del 60%, y su coste es de " , round (numerobarras * precio * preciodescuento , 2) , "euros")