#---------------OPERADORES DE ASIGNACIÓN ABREVIADOS: ------------------
# son operadores que nos asignan un valor a una variable.
x , y , z , w, p , q ,r = 10 , 10, 10 , 10 , 10 , 10 , 2 #me asigna el valor 10 a la variable x, etc 

#operador de asignacion suma:
print (x, y, z)
x += 1 # <> x =  x + 1
print(x) #el valor será 11, le suma 1 

#operador de asignacion de resta:
y -= 1 # <> y 0 y - 1 
print (x,y) #el valor será 10 y no 11, le resta 

#operador de asignacion de multiplicacion:
z *= 2 # <> z 0z * 2 
print (x, y, z) #vemos que por un lado tenemos 10 y por otro 20

#operador de asignacion de division:
w /= 2 # <> w = w / 2
print( x, y, z , w) 

#operador de asignacion de division entera:
p //= 2 # <> p = p // 5
print( x, y, z , w, p) 

#operador de asignacion de resto:
q %= 2 # <> q = q % 5
print( x, y, z , w, q ) 

#operador de asignacion de exponenciación:
r **= 2 # <> r = **2
print( x, y, z , w , q , r) 


#----------------OPERADORES DE COMPARACION: ---------------
#tengo variables asociadas a valores que con los operadores de comparacion se preguntan cosas )comparar dos elementos):
a , b , c , A = 10 , 4 , 3 , 10.0

#operador de comparacion de igualdad: compara el valor de las dos variables, que sea la misma cantidad 
#en este caso son distintos 
print (a==b) 

#operador de comparacion de identidad: verifica si las dos referencias apuntan al mismo objeto en memoria, es decir
#si son identicos, en este caso no son iguales ya que a= 10 y A = 10.0
print (a is A) #este operador === en las nuevas versiones de py, es lo mismo que poner is. 

#operador de comparacion de desigualdad: comparará si son diferentes los valores, no el formato
print (a !=A) #tienen el mismo valor, distinto formato
print (a != 10.1) #tienen distinto fvalor

#operador de comparacion estricto: hacen referencia a valores.
print (A > a ) #la operacion de toda la vida en cuanto a los valores que tienen asociados las variables
print (A < a)

#operadores de comparacion pseudoestrictos: hacen referencia a valores.
print (A >= a)
print (A <= a)

