print("First Task")

a_int = 23
a_fl = 32.65
a_str = "a string"
a_bool = True

print("INT=%d, FLOAT=%.3f, STRING=%s, BOOL=%s" %(a_int,a_fl,a_str,a_bool))

b_int = int(input("input b_int\n"))
b_fl = float(input("input b_fl\n"))
b_str = input("input b_str\n")
b_bool = bool(input("input b_bool\n"))

print("INT=%d, FLOAT=%.3f, STRING=%s, BOOL=%s" %(b_int,b_fl,b_str,b_bool))

print("%d+%d=%d" %(a_int,b_int,a_int+b_int))
print("%.3f*%.2f=%.5f" %(a_fl,b_fl,a_fl*b_fl))
print("%s%s" %(a_str,b_str))
print("%s or %s=%s" %(a_bool,b_bool,a_bool and b_bool))