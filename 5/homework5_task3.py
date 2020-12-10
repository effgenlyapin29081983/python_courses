f_name = input("Enter name text file:\n")
try:
    with open(f_name, 'r') as txt_file:
        num_string = 0
        sum = 0
        for line in txt_file:
            if float(line.split()[1]) < 20000:
                print(line.split()[0])
            sum += float(line.split()[1])
            num_string += 1
        print("average ZP = %.2f" %(sum/num_string))
except IOError:
    print("input\output error!")