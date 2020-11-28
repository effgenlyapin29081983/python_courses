month = int(input("Month[1..12]\n"))
seasons_dict = {1:"Winter",2:"Winter",3:"Spring",4:"Spring",5:"Spring",6:"Summer",7:"Summer",8:"Summer",9:"Autumn",10:"Autumn",11:"Autumn",12:"Winter"}
seasons_list = ["Winter","Winter","Spring","Spring","Spring","Summer","Summer","Summer","Autumn","Autumn","Autumn","Winter"]
if ((month<1) or (month>12)):
    print("month out of range")
    exit()
else:
    print("Dictionary Value = %s" %(seasons_dict.get(month)))
    print("List Value = %s" %(seasons_list[month-1]))

