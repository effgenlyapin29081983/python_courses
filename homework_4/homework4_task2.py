from random import randint

length = int(input("Enter length list:\n"))
new_list = [randint(0, 500) for el in range(0, length)]
print("Generated list:\n", new_list)
my_list = [new_list[i] for i in range(1, length) if new_list[i] > new_list[i - 1]]
print("New list:\n", my_list)
