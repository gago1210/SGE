# (11.09.24)
#python es sensible a mayusculas y minusculas !!
#TIPOS DE DATOS: (utilizamos type para ver el tipo de dato)
    # 1.NUMERICOS
        ## ENTEROS: 3
        ## ECIMALES: 3.3

            # OPERACIONES CON DATOS NUMÉRICOS
                ## SUMA: +
                ## RESTA: -
                ## MULTIPLICACION: *
                ## DIVISION DECIMAL: /
                ## DIVISION ENTERA: //
                ## MODULO: (ES EL RESTO) %
                ## POTENCIA, ELEVAR UN NUMERO: **

x = 3
y = 2
print (3*2) # x*y = 6
print (x*y) # 3*2 = 6

print (x/y) # 3/2 = 1.5 (division decimal)
print (x//y) # 3//2 = 1 (division entera)
print (x%y) # es el resto de la division 3/2
print (x**y) # 3elevado a 2= 9

#si lo que yo hago es declarar asi, al ser el dividendo un numero decimal, el resultado es una de las excepciones,
# va a ser un valor decimal.
a = 3
b = 2.1
print (3*2.1) # a*b = 6.3
print (a *b) # 3*2.1 = 6.3

print (a/b) # 3/2.1 = 1.4285... (division decimal)
print (a//b) # 3//2.1 = 1 (division entera) 
print (a%b) # es el resto de la division 3/2 = 0.8999....

#si lo que yo hago es declarar asi, al ser el dividendo un numero decimal, el resultado es una de las excepciones,
# va a ser un valor decimal.
c = 3.1
d = 2
print (3.1*2) # c*d = 6.2
print (c *d) # 3*2 = 6.2

print (c/d) # 3.1/2 = 1.55 (division decimal)
print (c//d) # 3.1//2 = 1 (division entera) 
print (c%d) # es el resto de la division 3.1/2 = 1.1

#si yo decido hacer una operacion como 3*2 que me da 6 y, tambien la supuestamente operacion identica 3.0*2 que me da 6.0
#no son lo mismo por que una es un numero entero y la otra uno decimal, tecnicamente pàrece lo mismo, pero no lo es.
#lo veremos en la proxima clase, ejercicio 2.

#(17.09.24)
# en python hay una instruccion que es type, la cual sirve para coger informacion de esa instruccion, el tipo de dato
# (necesito print para imprimir el resultado).
print (type (x*y))
#cuando programamos con python, este programa tiene una tendencia a progarmar objetos, cuando ejecutamos hasta lo anterior
#type nos da la informacion de ''class 'int' '',lo cual es por esa tendencia a la programacion de objetos de manera
#secuencial de objetos, de ahi que la informacion nos aparezca como ''class''.

#¿como definimos una variable en python? el interprete determina directamente el tipo.
#¿podriamos hacer una declaracion de variables todas seguidas en la misma linea? si, la unica condicion es que si pongo 
#dos variables, les de los valores separados por las comas como en el ejemplo, se denomina declaracion simultanea
# de variables, de esta manera es lo mismo:
e=3
f=4 

g,h = 5,6

#lo comprobamos parta ver si funciona y si, correctamente:
print (g*h)


#continuacion de tipo de datos:
    #2.STRINGS (CARACTERES): son alfanumericos, es decir, el abecedario, los numeros, los caracteres especiales, cualquiera
    #que esté en la tabla ASCII. Para definir un alfanumerico, se utiliza las comillas simples '' o las comillas dobles "". 
    #No se pueden combinar las dos, si utilizo un String con una comilla simple, lo acabo como tal.
    #vamos a tener distintos tipos de string:
        #CARACTERES ABECEDARIO: Aa (tipo string)
        #CARACTERES ESPECIALES: * , !, $ <>, (tipo string)
    
z, w = 'a',"a"
print (type (z)), type ((w))
#en el ejemplo, hemos podido definir de las dos maneras un string.
#tambien podemos escribir dependiendo de las comillas, esto se llama concatenación.
print ("hola 'jose' ")
print ('hola "jose"')
#si queremos que salga en otra linea podemos utilizar dos metodos, el salto y/o la triple comilla:
print ("""hola 
       jose """)
#¿puedo multiplicar strings? si, jjjj:
print ("j" * 4)
#podemos hacer suma de caracteres (a+b)para que me salga ab:
print ("k"+"l")
#si decido sumar con un valor decimal, nos da error porque lo que queremos es repetir un caracter, un numero x de veces, 
#no tiene sentido que sea decimal, no se puede dividir por decima, tiene que ser entero:
print ("a" + "3.1")
#no se puede dividir un string entre un string, ni dividir un string entre un numero.

#si yo quiero interaccionar, de manera que el usuario meta algo por teclado, usamos la instruccion input, de esta manera se recibe la informacion:
g = input ("Edad")
print (g, type(g))
#si yo recupero la informacion con print, lo que ocurrirá es que nos lo guarda input la introduccion por teclado, en formato string.
#¿como creo un codigo 


    #3.BOOLEANO/LOGICOS: verdadero (true, 1 ) o falso (false, 0). 
m, n = True, False
print (m) #me sale true
print (n) #me sale false
#si quiero ver que valor tiene una de las variables:
print (type(m)) #me saldrá el valor
#¿que pasa si en type introduzco un 1? ya que se supone que 1 corresponde a true...
print (type(1)) #me saldra 'class int' 
#¿como puedo convertirlo a un true? lo tengo que castear, cohercion:
print (bool (1)) #esto se hace cuando quiero convertir un numero a un valor logico como en este caso, 1.

    #4.ESTRUCTURA CONTENEDORA DE DATOS: listas = listas; diccionadios = dic; (25/10/24)
        #4.1. LISTAS: (poner corchetes)
        # una lista es una secuencia de datos mutable, con la que puedo cambiar el contenido de la misma.
        # la lista va dentro de corchetes y separada entre comas:
o = ["1" , 1, 1.0]
print (o)

        #¿como puedo saber que cantidad de elementos tiene una lista? a traves de la funcion avanzada len:
        #str es el casteo, puedo pasar de un tipo de dato a otro tipo de dato a traves de el.
print ("cantidad de elementos de la lista ", str(o), "son", str (len (o)), "elementos") 
        #esto es lo mismo: 
print (type (o))
print ("cantidad de elementos de la lista " +str(o)+ "son" +str (len (o)) +"elementos") 

        #¿como puedo acceder a los elementos de la lista? a traves de los indices:
        # los indices siempre empiezan en 0 y llegan hasta el valor de len en la lista -1:
print (o[0],type(o[0]))
print (o[len (o)-1],type(o[len(o)-1]))
        #esto es lo mismo:
print (o[2]), type (o[2]) #esto es 3 en el indice 0 y -1 del ultimo.

        #¿como puedo añadir valores a la lista?
        #tengo una funcion de alto nivel con un metodo: append, en el cual solo puedo meter un valor, solo uno, nunca varios.
        #en el ejemplo, vamos a meter otra lista, con la palabra amigo:
o.append(["amigo", True])
print(o)
        #si yo quiero meter false:cc
o[3].append ("False")
print (o)

        #4.2. TUPLAS --> () TUPLE
        # las tuplas son elementos ordenados, estan indexados, tienen indices, pero tienen una diferencia en comparacion con las listas y es que 
        #las tuplas me permite trabajar con mas datos, pero no puedo cambiar el contenido de la tupla, es fijo, es inmutable.
        #las tuplas son heterogeneas, ordenadas, inmutables, lo cual implica que podemos guardar elementos que principalmente no tienen que
        #cambiar. 
        #la principal ventaja que tienen en comparacion con las listas es que las tuplas son mucho mas rapidas y eficientes, en un contexto en el 
        #que yo voy a guardar datos, que no vayan a ser modificados, voy a aumentar la eficiencia.
f, F =(3,4), tuple ()
print (f, type(f), "..", F, type (f))
print ("La longitud de la tupla es", len(f))
f[1] = "1" #da un error por inmutabilidad
print (f)

        #4.2.1. OPERACIONES CON TUPLAS:
        #Se puede utilizar para saber si esta contenida la lista en la tupla. Recuperamos la letra q y preguntamos si existe la letra a en la q.
print(3 in f)
        #se pueden sumar dos tuplas??:
        #creamos dos tuplas, no existe la suma pero si la concatenacion que al final lo que se hace es meter los elementos dentro.
print ("a" in f)
print ([1,2]+ [2,3]) #concatenacion, no suma.

        #se puede multiplicar dos tuplas??:no, no existe la multiplicacion de tuplas.


        #4.3. DICCIONARIOS (dict - {}): es una estructura que me va a dar siempre un valor consistente en una lista de parejas de variables
        # clave - valor, por la que cada uno de los elementos clave, que puede ser de cualquier tipo de dato, va a tener 
        #asociado siempre cualquier tipo de valor que tambien puede ser cualquier tipo de dato.

        #los diccionarios son heterogeneos y son mutables, es decir, los puedo cambiar.
q = {}
print(q, type (q))
        #ejemplo:
q = {1:"1", 2:"2"} #valor asociado de 1 numerico, 1 en string, valor asociado al numero 2 en numerico, 2 en string
print(q, type (q)) #es heterogeneo porque podemos guardar cualquier cosa, una lista, otro diccionario, podemos anidar.

        #¿como podemos saber la cantidad de elementos que tienen? con len: (1/10/24)
print ("cantidad de elementos del diccionario", str (q), "son", str (len(q)), "elementos") 
        #puedo acceder al contenido de la lista si meto el valor de la clave y tambien saber el tipo de dato (las estructuras clave valor, 
        # al tener introducida la clave buscamos que nos localice ese elemento en la memoria):
print(q[1], type (q[1]))

#esto son las estructuras internas que tiene python.