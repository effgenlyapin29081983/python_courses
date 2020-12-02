def output_info(var_name, var_surname, var_year, var_city, var_email, var_phone):
    print("{0} {1}({2}): {3}; {4}; {5}.".format(var_name, var_surname, var_year, var_city, var_email, var_phone))


list_keys = ["Name", "Surname", "Year", "City", "Email", "Phone"]
list_values = []
for el in list_keys:
    list_values.append(input("Enter {0}:\n".format(el)))

output_info(list_values[0], list_values[1], list_values[2], list_values[3], list_values[4], list_values[5])
