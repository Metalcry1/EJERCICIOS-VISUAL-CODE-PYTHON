
print('Por favor introduce las edades de los asistentes \n')

baby_pryce = 0
menores_pryce =  14
adultos_pryce =  23
jubilados_pryce =  18


def franja_edad():
    edades= list()
    edad = 1
    baby = 0
    menores = 0
    adultos = 0
    jubilados = 0
    
    while edad != 0:
        edad = int(input())
        edades.append(edad)
        if edad in range (1,15):
            baby += 1
        elif edad in range (15,18):
            menores += 1
        elif edad in range (18,65):
            adultos += 1
        elif edad >=65:
            jubilados += 1
        elif edad == 0:
            break
    return edades, edad, baby, menores, adultos, jubilados   

edades, edad, baby, menores, adultos, jubilados = franja_edad()




print('{} entradas de baby (0€): {}'.format(baby,(baby*baby_pryce)))
print('{} entradas de menores (14€): {}'.format(menores,(menores*menores_pryce)))
print('{} entradas adultos (23€): {}'.format(adultos,(adultos*adultos_pryce)))
print('{} entradas jubilados (18€): {}'.format(jubilados,(jubilados*jubilados_pryce)))




