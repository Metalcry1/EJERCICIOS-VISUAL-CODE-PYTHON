
#Ejercicio 2

def calculate():
    my_dict = dict()

    my_dict = {"Nombre":[],"Edad":[],"Direccion":[]}

    name = input('Cual es tu nombre\n')
    name = name.lower().capitalize()
    age = input ('Cual es tu edad\n')
    age = age.lower().capitalize()
    direcction = input('Cual es tu direccion\n')
    direcction = direcction.lower().capitalize()

    my_dict['Nombre'].append(name)
    my_dict['Edad'].append(age)
    my_dict['Direccion'].append(direcction)
    
    print(my_dict)
    print(my_dict['Nombre'])
    print(my_dict['Edad'])
    print(my_dict['Direccion'])

#my_dict = calculate()

#Ejercicio 3

def calculate_fruit():
    
    fruits = dict()
    fruits = {'Platano': 1.35,'Manzana': 0.80,'Pera':0.85,'Naranja':0.70}

    type_fruit = input('Que fruta quieres\n')
    if type_fruit in fruits:

        qy_fruit = int(input('Cuantos kilos quieres\n'))

        def calculate(qy_fruit):
            if type_fruit:
                qy_fruit =  qy_fruit * fruits[type_fruit]
                return qy_fruit

        type_fruit = type_fruit.lower().capitalize()
        print('Te saldra el total de {} por {} €'.format(type_fruit,calculate(qy_fruit)))
    else:
        print('No disponemos de esa fruta')

calculate_fruit()

