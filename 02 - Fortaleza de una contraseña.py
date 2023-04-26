

def validaPwd(password):
    #password = '12345678a)'
    password_to_list = list(password)
    password_number = 0
    lower_character = 0
    isalpha_character = 0
    if len(password) < 8:
        print("Debe contener 8 digitos al menos")
        password += 1
    else:
        #print('Contraseña debil contiene 8 numeros')
        for elements in password_to_list:
            if (elements.islower()):
                #print('Contraseña fuerte contiene letras y 8 numeros')
                lower_character += 1 

        for elements in password_to_list:
            if (not elements.isalpha() and not elements.isdigit() ):
                #print('Contraseña muy fuerte contiene caracteres especiales')
                print(elements)
                isalpha_character += 1 


        if lower_character== 0:
            print("Debe contener al menos una letra minuscula")
        if isalpha_character== 0:
            print("Debe contener al menos un caracter especial")

        if password_number and lower_character and  isalpha_character == 0:
            print('Contraseña debil contiene 8 numeros')
        elif lower_character and  isalpha_character == 0:
            print('Contraseña fuerte contiene letras y 8 numeros')
        elif isalpha_character == 1:
            print('Contraseña muy fuerte contiene caracteres especiales')


    #print(lower_character)
    #print(isalpha_character)

password = input('Introduce una contraseña: \n')
validaPwd(password)
