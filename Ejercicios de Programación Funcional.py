"""
Ejercicio 1
Escribir una función que aplique un descuento a un precio y otra que aplique el IVA
a un precio. Escribir una tercera función que reciba un diccionario con los precios 
y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice
la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y 
devolver el precio final de la cesta.
"""


basket = {'Memoria Ram': 75.00,'Placa base': 200.00,'Procesador':350.00,'Tarjeta grafica': 750.00}
basket_with_discount = dict()
basket_with_iva = dict()
total_basket = 0.0
total_with_discount = 0.0
total_with_iva = 0.0

def calc_total_basket():
    total_basket = 0.0
    for element in basket:
        total_basket = total_basket + basket[element]
    return total_basket


def calc_offer():
    total_with_discount = 0.0
    for element in basket:
        basket_with_discount[element]= basket[element] / 1.21
        total_with_discount = total_with_discount + basket[element] / 1.21
    return basket_with_discount,total_with_discount
    

def calc_iva():
    total_with_iva = 0.0
    for element in basket:
        basket_with_iva[element]= basket[element] / 1.21
        total_with_iva = total_with_iva + basket[element] * 1.21
    return basket_with_iva,total_with_iva


total_basket = calc_total_basket()
print('La cesta de la compra original',basket)
print('El total de la cesta de la compra original es: ',total_basket, '€')

print()

basket_with_discount, total_with_discount = calc_offer()
print('La cesta de la compra aplicado el descuento',basket_with_discount)
print('El total de la cesta de la compra con descuento es: ',total_with_discount, '€')

print()

basket_with_iva, total_with_iva = calc_iva()
print('La cesta de la compra aplicado el IVA',basket_with_iva)
print('El total de la cesta de la compra con IVA es: ',total_with_iva, '€')

""" OUTPUT
La cesta de la compra original {'Memoria Ram': 75.0, 'Placa base': 200.0, 'Procesador': 350.0, 'Tarjeta grafica': 750.0}
El total de la cesta de la compra original es:  1375.0 €
La cesta de la compra aplicado el descuento {'Memoria Ram': 61.98347107438017, 'Placa base': 165.28925619834712, 'Procesador': 289.25619834710744, 'Tarjeta grafica': 619.8347107438017}
El total de la cesta de la compra con descuento es:  1136.3636363636365 €
La cesta de la compra aplicado el IVA {'Memoria Ram': 61.98347107438017, 'Placa base': 165.28925619834712, 'Procesador': 289.25619834710744, 'Tarjeta grafica': 619.8347107438017}
El total de la cesta de la compra con IVA es:  1663.75 €
"""