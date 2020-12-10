seconds_var = int(input("seconds:\n"))

print("hh:mm:ss = {:>2}:{:>2}:{:>2}".format(seconds_var//3600,(seconds_var%3600)//60,seconds_var%60))