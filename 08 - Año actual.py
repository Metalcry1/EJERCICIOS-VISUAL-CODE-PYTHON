from datetime import datetime
now = datetime.now()
print(now)
actual_year = now.year
years_old= int(input('Cuantos años tienes?'))
retirement = int(input('A que edad te jubilarias'))
resultado = retirement - years_old
retirement_year = resultado + actual_year
print(' Te quedan: {} años para jubilarte \n Estamos en {} te jubilaras en {}'.format(resultado,actual_year,retirement_year))
