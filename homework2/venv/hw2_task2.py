list_var=[]
while 1>0:
    test_var = input()
    if test_var != "":
        list_var.append(test_var)
    else:
        break
for el in range(0,len(list_var) if len(list_var)//2==0 else len(list_var)-1,2):
    list_var[el], list_var[el+1] = list_var[el+1], list_var[el]
print(list_var)