f_name = input("Enter file name:\n")
try:
    with open(f_name,'w') as txt_file:
        while 1:
            inp_str = input("Enter string:\n")
            if inp_str != "":
                txt_file.write(inp_str+'\n')
            else:
                break
except IOError:
    print("input\output error!")