#LISTAS --> list() []
x , X = ["2" , 1 , "2" , 2 , "2" , 3 , [1,2,3]] , list()
print(f"Saber el numero de elementos de una lista len(x) = {len(x)}")
print(f"Para acceder al elemento inicial x[0] = {x[0]}")
print(f"Para acceder al ultimo elemento x[6] = {x[len(x)-1]}")
print(x[0:3]) #subseting de listas
print(x[0::2]) #subseting de listas con paso de 2
print(x[-1][1]) #esto es lo mismo que print(x[len(x)-1][1])


X.append(1) #añadir un elemento a una lista en la ultima posicion
X.append(2)
X.append(10)
X.append(1)
X.append(10)
X.append(1)
X.append(1)
X.append(3)
print(X)
X[0] = 0 #actualizar un valor de un indice
X.pop(2) #borrar el dato guardado en el indice que yo le paso (si no esta nos da error)
print(X)
X.remove(1)
print(X)
X.remove(1)
print(X)
X.remove(1)
print(X)
X.remove(1)
print(X)
print(f"Numero de ocurrencias del valor 1 en la lista X: {X.count(1)}")
X.reverse() #da la vuelta a la lista
print(X)



a , b = [2,4,6] , [8,10,12]
print(a , b) #concatenar las listas ---> [2,4,6,8,10,12]
print("-".join(["2" , "3" , "4"]))

c = [2,4,6] + [8,10,12]
d = c.copy() #copiar una lista en otra variable
d[0] = 80
print(d)