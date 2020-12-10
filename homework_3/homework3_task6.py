def int_func(var_str):
    var_list = list(var_str)
    var_list[0] = var_list[0].upper()
    return "".join(var_list)


input_list = input("Enter string:\n").split()
for i in range(0, len(input_list)):
    input_list[i] = int_func(input_list[i])
print(" ".join(input_list))
