
a = (1,2,3,4,5,6,7,8,9)
b = (1,2,3,4,5,6,7,8,9)

resultado = list(map(lambda a,b: a * b, a,b))
print(resultado)

num1 = 5
num2 = 5


def sum_two_numbers():
    return lambda num1, num2: num1+num2

print(sum_two_numbers()(num1,num2))


