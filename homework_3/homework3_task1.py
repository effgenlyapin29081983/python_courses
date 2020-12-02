def my_division(var1, var2):
    print("Division by zero!!!") if var2 == 0 else print("Result = ", var1 / var2)


a = int(input("Enter a:\n"))
b = int(input("Enter b:\n"))
my_division(a, b)
