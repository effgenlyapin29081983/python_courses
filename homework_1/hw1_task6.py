def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False
        
tmp_str = input("Введите дистанцию 1 дня\n")
if is_digit(tmp_str):
	dyst = float(tmp_str)
else:
	print("Дистанция не число!")
	exit()
	
tmp_str = input("Введите достижимую дистанцию\n")
if is_digit(tmp_str):
	dost_dyst = float(tmp_str)
else:
	print("Достижимая дистанция не число!")
	exit()
	
i=1
while dyst<dost_dyst:
	i+=1
	dyst+=dyst*0.1

print("На %d день будет достигнута дистанция %f >= %f" % (i, dyst, dost_dyst))
	