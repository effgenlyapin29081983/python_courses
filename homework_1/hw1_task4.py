str_num = input("Enter num\n")
def max_num(num : str)->int:
	max = int(num[0])
	i =1
	while i<len(num):
		if int(num[i])>max:
			max=int(num[i])
		i+=1
	return max

if int(str_num)<0:
	print("num<0")
else:
	print("Max num=", max_num(str_num))