#MANEJO DE STRINGS
x , y , z , w = 'a' , "a" , """a""" , '''a'''
print (x + y) #concatenacion de strings
print (x + 3) #repeticion de strings

e , n = 38 , "jose"
q = f"hola, {n} .  Tu edad es de {e} años" #casteo F-string
Q = "hola, {} .  Tu edad es de {} años".format(n,e) #casteo format, esto es otra forma de hacer lo de la linea anterior
g = "Hola, %s . Tu edad es %d años" %(n,e) #casteo con porcentaje
print(Q, type(Q))

#operaciones propias de los strings
i , c = 12345 , "Python"
print(len(c)) #cantidad de caracteres de un string
print(c[0] , c[1] , c[2] , c[3] , c[4] , c[5]) #acceso a los elementos del string por su indice
print(c[-1]) #accedo al ultimo caracter sin conocer su indice

#METODO SLICING [inicio = 0 : fin = len(<variable>) : paso 1] esto es lo equivalente a decirle  c[0 :6 :1]
print(c[0:len(c)])#me saca todos los elementos del indice 
print(c[0:len(c):2]) #para que me saque solo los elementos pares
print(c[0:len(c):3]) #para que me saque solo los elementos impares 

z = "Hola amigo     mio"
print(z, len(z))
print(z.upper()) #convierte todo a mayusculas
print(z.lower()) #convierte todo a minusculas
print(z.title()) #capitaliza las palabras de un string
print("hola amigo     Mio".capitalize()) #capitaliza la frase
print("hOLA".swapcase()) #intercambio de mayusculas a minusculas y viceversa

print(z.find("0")) #indice de la primera coincidencia de izquierda a derecha ¡¡puede haber mas coincidencias !! (si no hay coincidencia, devuelve -1)
print(z.rfind("o")) #indice de la primera coincidencia de derecha a izquierda ¡¡puede haber mas coincidencias !! (si no hay coincidencia, devuelve -1)
print(z.index("0")) #igual que find pero si no hay coincidencia, devuelve error
print(z.rfind("0")) #igual que rfind pero si no hay coincidencia, devuelve error

print(z.count("o",0,11)) #numero de coincidencias de un caracter en el intervlo definido del string
print("+31919190009".starswith('+31')) #comprueba que un string empieza de una determinada manera
print("+31919190009".endswith('09')) #comprueba que un string termina de una determinada manera

print("abcZ".isalpha()) #comprobar si todas las letras tienen mayusculas y minusculas
print("+31919190009".isdigit(), "91990009".isdigit()) #devuelve false si no es digitos
print("Es34001254568".isalnum()) #comprueba si hau numeros y letras (matusculas o minusculas)
print("hola".islower()) #comprueba si todo es minusculas
print("HOLA".isupper()) #comprueba si todo es mayusculas
print("Hola Amigos".istitle()) #comprueba si las palabras del string estan capitalizadas
print("ç".isascii()) #comprueba que todos los caracteres del estring son ascii

print("amigO miO".replace("O","o")) #reemplazar caracteres
print("hola".strip() , len("hola".strip())) #eliminar todos los espacios de inicio a fin
print("hola".rstrip() , len("hola".rstrip())) #eliminar todos los espacios a fin
print("hola".lstrip() , len("hola".lstrip())) #eliminar todos los espacios a inicio 
print(",".join(["platano" , "fresa" , "uvas"])) #une los elementos de una lista con un separador definido
print("533232".zfill(9)) #rellena con ceros a la izquierda hasta completar el numero de caracteres faltantes respecto del numero que defino
print("a\tb".expandtabs(1)) #transformar el tabulador al numero de aespacios definido

print("inicio programa".center(30, "*")) #centrar el texto en un ancho fijo de caracteres
print("inicio programa".ljust(30, "*")) #ajustar el texto a la izquierda en un ancho fijo de caracteres
print("inicio programa".rjust(30, "*")) #ajustar el texto a la derecha en un ancho fijo de caracteres

print("Juan, Mercedes, Alberto".split(", ")) #dividir el string de izquierda a derecha por el elemento indicado guardandolo en una lista
print("Juan, Mercedes, Alberto".rsplit(", ")) #dividir el string de derecha a is¡zquierdaa por el elemento indicado guardandolo en una lista
print("Hola Maria n\¿qué tal estas?".splitlines()) #dividir cada linea en un elemento de la lista
print("Juan, Mercedes, Alberto".partition(", ")) #divide cualquier string en tres trozos de izquierda a derecha pasandolo a tupla
print("Juan, Mercedes, Alberto".rpartition(", ")) #divide cualquier string en tres trozos de derecha a izquierda pasandolo a tupla

