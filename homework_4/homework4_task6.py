from mod_count import my_count
from mod_cycle import my_cycle
from random import random
from random import randint

print("Executing my_count:\n")
print(my_count(int(input("enter begin num:\n")), int(input("Enter stop num:\n"))))

print("Executing my_cycle:\n")
print(my_cycle([random()*3*7/4+6 for el in range(0, randint(1, 100))], int(input("Enter repeats num:\n"))))