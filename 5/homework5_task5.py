from random import randint
from functools import reduce


def gen_num_str():
    new_list = [str(randint(0, 500)) for el in range(0, randint(1, 100))]
    return " ".join(new_list)


def sum_els(a, b):
    return int(a) + int(b)


f_name_out = input("Enter name output text file:\n")
try:
    with open(f_name_out, 'w') as txt_file_out:
        txt_file_out.write(gen_num_str())

    with open(f_name_out, 'r') as txt_file_out:
        print("sum elements = ", reduce(sum_els, txt_file_out.readline().split()))
except IOError:
    print(r"input\output error!")
