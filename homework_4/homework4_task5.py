from random import randint
from functools import reduce


def mul(prev_el, el):
    return prev_el * el


length = int(input("Enter length list:\n"))
my_list = [randint(100, 1001) for el in range(0, length)]
print("Input list", my_list)
print("Result list:\n", reduce(mul, my_list))
