from math import factorial


def gen(a):
    for els in range(1, a+1):
        yield els


g = gen(int(input("Enter num:\n")))

for el in g:
    print(factorial(el))
