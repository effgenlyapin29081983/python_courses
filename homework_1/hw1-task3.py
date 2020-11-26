num_var = int(input("input num:\n"))
range_var = int(input("input range:\n"))

def form_num(n, r):
	if r>0 and n>0:		
		i = 1
		temp_str =""
		while i<=r:
			temp_str+=str(n)
			i+=1		
		return int(temp_str)
	else:
		return 0
	
def summ_num(n,r):
	summ = 0
	if r>0 and n>0:
		i = 1
		while i<=r:
			summ+=form_num(n,i)
			i+=1
	return summ
			
print("summ_num=", summ_num(num_var, range_var))