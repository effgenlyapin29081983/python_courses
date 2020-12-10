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
            temp_val =temp_dict.pop(temp_key)
            if temp_val >= 0:
                av_prib += temp_val
            count += 1
        dict_av_prib={"average_prib":av_prib/count}
        my_list=[]
        my_list.append(my_dict)
        my_list.append(dict_av_prib)
        print(my_list)
    with open(f_name+".json", 'w') as json_file:
        json.dump(my_list, json_file)
except IOError:
    print(r"input\output error!")

