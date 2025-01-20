#CONDICIONAL

"""sintaxis:
if <condicion>:
|   <<codigo_en_caso_True_de_la_condicion>>
else:
|   <<codigo_en_caso_False_de_la_condicion>>
"""
x = 12

if x <= 13:
    print(f"{x} es menor o igual a 13")
else:
    print(f"{x} es mayor a 13")
    



"""sintaxis:
if <condicion_1>:
|   <<codigo_en_caso_True_de_la_condicion_1>>
elif <<condicion_2:
|   <<codigo_en_caso_True_de_la_condicion_2>>
.
.
.
.
elif <condicion_n-1:
|   <<codigo_en_caso_False_de_las_condiciones_no_se_cumplan>>
"""  
y = 6
if y == 1:
    print(f"y = {y} (1)")
elif y == 2:
    print(f"y = {y} (2)")
elif y == 3:
    print(f"y = {y} (3)")
elif y == 4:
    print(f"y = {y} (4)")
elif y == 5:
    print(f"y = {y} (5)")
elif y == 6:
    print(f"y = {y} (6)")
else:
    print(f"y = {y} , y no es ni 1, ni 2, ni 3, ni 4, ni 5, ni 6")

    
    