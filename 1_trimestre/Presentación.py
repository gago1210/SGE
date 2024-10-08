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
#tambien podemos escribir dependiendo de las comillas:
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

    #BOOLEANO/LOGICOS: verdadero (true, 1 ) o falso (false, 0). 
m, n = True, False
print (m) #me sale true
print (n) #me sale false
#si quiero ver que valor tiene una de las variables:
print (type(m)) #me saldrá el valor
#¿que pasa si en type introduzco un 1? ya que se supone que 1 corresponde a true...
print (type(1)) #me saldra 'class int' 
#¿como puedo convertirlo a un true? lo tengo que castear, cohercion:
print (bool (1)) #esto se hace cuando quiero convertir un numero a un valor logico como en este caso, 1.