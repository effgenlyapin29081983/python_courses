
def my_func(a):
    var_res = 1
    def mul_func():
        nonlocal var_res
        var_res *= a
        return var_res
    return mul_func


var_a = int(input("Enter a:\n"))
abs(var_a)
var_b = int(input("Enter b:\n"))
if var_b > 0:
    var_b *= -1
if var_a!=0:
    print("{0}**{1}={2}".format(var_a, var_b, var_a ** var_b))
    print("pow({0},{1})={2}".format(var_a, var_b, pow(var_a, var_b)))
    var_x = 0
    func_obj = my_func(var_a)
    for i in range(2, abs(var_b)+2):
        var_x = func_obj()
    print("my_pow({0},{1})={2}".format(var_a, var_b, 1/var_x))
else:
    print("Division by zero!!!")