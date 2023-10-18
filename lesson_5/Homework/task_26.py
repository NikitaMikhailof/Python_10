# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def raise_to_degree(a, b):
    if b == 0:
        return 1
    return a * raise_to_degree(a, b-1)

print(raise_to_degree(2, 5))

