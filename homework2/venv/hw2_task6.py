list_var = []
i = 1
while 1 > 0:
    temp_name = input("Enter name:\n")
    if temp_name == "":
        break
    else:
        temp_list = []
        temp_list.append(i)
        temp_dict_nom = {"name": temp_name}
        temp_dict = {"price": float(input("Enter price:\n"))}
        temp_dict_nom.update(temp_dict)
        temp_dict = {"quantity": int(input("Enter quantity:\n"))}
        temp_dict_nom.update(temp_dict)
        temp_dict = {"units": input("Enter units:\n")}
        temp_dict_nom.update(temp_dict)
        temp_list.append(temp_dict_nom)
        list_var.append(tuple(temp_list))
        i += 1

print(list_var)
list_names = list_prices = list_quantities = []
set_units = set()
for el in range(0, len(list_var)):
    list_names.append(list_var[el][1].get("name"))
    list_prices.append(list_var[el][1].get("price"))
    list_quantities.append(list_var[el][1].get("quantity"))
    set_units.add(list_var[el][1].get("units"))
print("Output dictionary:")
print({"name": list_names, "price": list_prices, "quantity": list_quantities, "units": set_units})
