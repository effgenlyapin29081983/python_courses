string_var = input("input string:\n")
list_var=string_var.split()
for el in range(0,len(list_var)):
    print(el,'{:.10}'.format(list_var[el]))