import json
def calc_prib(source_str):
    my_list = source_str.split()
    prib = float(my_list[2]) - float(my_list[3])
    tmp_dict = {my_list[0]: prib}
    return tmp_dict, my_list[0]


f_name = input("Enter name file:\n")
my_dict = {}
av_prib = 0
count=0
try:
    with open(f_name, 'r') as txt_file:
        for line in txt_file:
            temp_dict, temp_key = calc_prib(line)
            my_dict.update(temp_dict)
            print(temp_dict)
            temp_val =temp_dict.pop(temp_key)
            print(temp_val)
            if temp_val >= 0:
                av_prib += temp_val
            count += 1
        my_dict.update({"average_prib":av_prib/count})
        print(my_dict)
    with open(f_name+".json", 'w') as json_file:
        json.dump(my_dict, json_file)
except IOError:
    print(r"input\output error!")
print(my_dict)
