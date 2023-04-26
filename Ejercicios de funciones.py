#EJERCICIO 1

def salute_call():
    def salute ():
        print('Hola amiga')

    salute()
    salute()
    salute()

#salute_call()

#EJERCICIO 2

def Salute_call2():
    def salute(name):
        print('Hola {}'.format(name))

    name = input("Cual es tu nombre\n")
    salute(name)

#Salute_call2()

#EJERCICIO 3

def calc_factorial():
    def numb(number):
        factorial = number * number
        return factorial

    number = int(input('Indica un numero entero para calcular su factorial\n'))
    factorial : int
    print(numb(number))

#calc_factorial()

#EJERCICIO 4

def iva_calculator():
    def calc_iva (invoice,iva):
        invoice_iva = invoice * iva
        return invoice_iva


    invoice = float(input('Indica el importe de la factura a calcular el IVA \n'))
    iva = 1.21

    print('La factura sin IVA es {} y con IVA es {}'.format(invoice,calc_iva(invoice,iva)))

#iva_calculator()

#EJERCICIO 5

def list_cuadrados_calculate():
    list_original = {2,3,4,5,6,7}
    list_new = list()
    print(type(list_original))
    def calculate_cuadrado ():
        for element in list_original:
            element *= element
        
            list_new.append(element)
    
    
        print(list_original)
        print(list_new)
    calculate_cuadrado ()

#list_cuadrados_calculate()

#EJERCICIO 6

lista = list()
contador = 0
my_dict = dict()

def new_func(lista, contador, my_dict):
    while contador < 5:
        valor = input('Indica una palabra\n')
        lista.append(valor)
        str_contador = str(contador)
        my_dict[str_contador]=valor
        contador+=1

new_func(lista, contador, my_dict)
    

def tupling(my_dict):
    print()

    

print(lista)
print(my_dict)


