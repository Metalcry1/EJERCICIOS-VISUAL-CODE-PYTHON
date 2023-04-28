
cadena_ini = input('Indica un texto a invertir\n').upper()
#cadena_ini = cadena_ini.upper()
cadena_final = ''
def fun_reverse(v,cadena_final):
    i =1
    while i <= len(cadena_ini):
        cadena_final +=cadena_ini[-i]
        i += 1
        
    return(cadena_ini,cadena_final)
print(fun_reverse(cadena_ini,cadena_final))