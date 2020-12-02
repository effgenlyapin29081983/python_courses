def sum_func(var_sum, var_slag):
    return var_sum+int(var_slag)
slag = ''
summa = 0
while slag!='q':
    for el in input("Enter numeric string, separator=probel, exit 'q':\n").split():
        if el == 'q':
            slag = 'q'
        else:
            summa = sum_func(summa, int(el))
    print(summa)

