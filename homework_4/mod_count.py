from itertools import count

def my_count(beg_num,stop_num):
    for el in count(beg_num):
        if el > stop_num:
            break
        else:
            print(el)