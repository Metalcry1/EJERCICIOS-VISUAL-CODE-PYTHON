import MODULO_ESTADISTICAS


texto = input('Indica un texto a contar \n')

caracteres = MODULO_ESTADISTICAS.contar_caracteres(texto)
palabras =  MODULO_ESTADISTICAS.contar_palabras(texto)
vocales =  MODULO_ESTADISTICAS.contar_vocales_y_consonantes(texto.lower())
especiales =  MODULO_ESTADISTICAS.contar_especiales(texto)