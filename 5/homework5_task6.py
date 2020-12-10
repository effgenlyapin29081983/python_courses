def concat(*args, sep=" "):
    return sep.join(args)

def prepare_string(source_str):
    mask = {r"(л)", r"(пр)", r"(лаб)", r"-", r":"}
    for el in mask:
        source_str = source_str.replace(el, "")
    temp_list = source_str.split()
    sum = 0
    for i in range(1, len(temp_list)):
#        if temp_list[i] != "":
         sum += int(temp_list[i])
    tmp_dict = {temp_list[0]:sum}
    return tmp_dict


f_name=input("Enter name file:\n")
my_dict={}
try:
    with open(f_name, 'r') as txt_file:
        for line in txt_file:
            my_dict.update(prepare_string(line))
except IOError:
    print(r"input\output error!")
print(my_dict)
