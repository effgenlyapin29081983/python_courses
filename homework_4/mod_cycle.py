from itertools import cycle

def my_cycle(var_list,num_repeats):
    x = 0
    for el in cycle(var_list):
        if x > num_repeats*len(var_list):
            break
        print(el)
        x += 1