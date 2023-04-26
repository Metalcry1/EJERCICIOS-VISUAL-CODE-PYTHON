cadena = 'Cadena'
largo_cadena = len(cadena)
space = ' '
space_white = ''

def more_space(space,space_white):
    contador=0
   
    while contador <= largo_cadena-1:
        space_white += space
        contador= contador+1
    return space_white


cadena= more_space(space,space_white) + cadena

print(len(cadena))
print(cadena)