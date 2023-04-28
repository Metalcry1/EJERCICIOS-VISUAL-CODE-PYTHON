#NUMEROS PRIMOS

num_1 = 2
primos =[]

def is_prime(num_1, primos):
    for i in range(0,101):
        if num_1 % 2 == 0 and num_1 != 2:
            print(num_1)
        elif num_1 % 3 == 0 and num_1 != 3:
            print(num_1)
        elif num_1 % 5 == 0 and num_1 != 5:
            print(num_1)
        elif num_1 % 7 == 0 and num_1 != 7:
            print(num_1)
        else:
            print(num_1, 'es primo')
            primos.append(num_1)
        num_1 += 1

is_prime(num_1, primos)
    

print(primos)

