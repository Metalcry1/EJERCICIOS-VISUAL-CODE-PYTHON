vocals = {'a','e','i','o','u','A','E','I','O'}
especiales = {'.',';',':','¡','!','¿','?','(',')','[',']','-','_','%'}

def contar_caracteres(texto):
    numero_caracteres = len(texto)
    print('El numero de caracteres es: ',numero_caracteres)

def contar_palabras(texto):
    numero_palabras = len(texto.split())
    print('El numero de palabras es:',numero_palabras)

def contar_vocales_y_consonantes(texto):
    numero_vocales = 0
    numero_consonantes = 0
    for letra in texto:
        if letra in vocals:
            numero_vocales += 1
        else:
            if letra.isalpha():
                numero_consonantes+= 1
    print('El numero de vocales es:',numero_vocales)
    print('El numero de consonantes es:',numero_consonantes)

def contar_especiales(texto):
    numero_especiales = 0
    for letra in texto:
        if letra in especiales:
            numero_especiales += 1
    print('El numero de especiales es:',numero_especiales)