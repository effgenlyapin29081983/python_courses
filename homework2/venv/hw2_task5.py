list_var = []
while 1>0:
    test_int = input("Enter natural num:\n")
    if test_int!="":
        list_var.append(int(test_int))
    else:
        break
list_var.append(int(input("Enter new num:\n")))
list_var.sort(reverse=True)
print(list_var)

