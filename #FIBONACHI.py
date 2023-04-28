#FIBONACHI

num = 0
num1 = 1
temp = 0
contador = 0

def fibonachi (num,num1,temp,contador):
    lista = []
    while contador <= 50:
        print(num)
        lista.append(num)
        temp = num + num1
        num = num1
        num1 = temp
        contador += 1
    print(lista)    

fibonachi(num,num1,temp,contador)
