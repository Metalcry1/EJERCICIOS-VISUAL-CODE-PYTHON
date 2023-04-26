import random

deportes = list()
deportes = ('Ciclismo','Submarinismo','Running','Tenis')
nuevo_valor = list()
posicion = random.randint(0,len(deportes)-1)
contador= 0
def myReplace(cadena,posicion,nuevo_valor):
    print(cadena[posicion])
    nuevo_valor = cadena[posicion]
    return nuevo_valor

print(nuevo_valor)


while contador <= len(deportes):
    nuevo_valor.append(myReplace(deportes,posicion,nuevo_valor))
    contador += 1
    #print(contador)
#print(nuevo_valor)
