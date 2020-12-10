f_name = input("Enter name text file:\n")
try:
    with open(f_name, 'r') as txt_file:
        num_string = 0
        for line in txt_file:
            print("words = ", len(line.split()))
            num_string += 1
        print("num strings = ", num_string)
except IOError:
    print("input\output error!")
