def my_func(a, b, c):
        var_list = [a, b, c]
        var_list.sort(reverse=True)
        return var_list[0]+var_list[1]


print("Result = ", my_func(int(input("a -\n")), int(input("b -\n")), int(input("c -\n"))))
