#DICCIONARIOS --> dict() {clave : valor}

d , D = {"1":1 , 1:"1" , 2:"2" , "2":2} , dict()

print(d.get("1"), type(d.get("1"))) #esto es lo mismo que print(d["1"], type(s["1"])) recupero el valor de una clave

d["1"] = "uno"
print(d["1"])

D.update({"3":3 , 3:"3"}) #añadir clave valor a un diccionario creado
print(D)
D.update({"3":"tres"}) #si la clave existe modifica el valor asociado
print(D)

print(d.keys())
print(d.values())

print(d)
d.clear() #vacia un diccionario
print(d)

c = d.copy() #copiar el diccionario a otra variable

g , G = [6 , 7] , ["6" , "7"] , "rellename"
f = dict.fromkeys(g , G)
print(f)
