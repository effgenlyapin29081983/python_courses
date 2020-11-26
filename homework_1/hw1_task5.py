def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

tmp_str = input("Введите размер выручки\n")
if is_digit(tmp_str):
	vir_val = float(tmp_str)
else:
	print("Выручка-не число")
	exit()

	
tmp_str = input("Введите размер издержек\n")
if is_digit(tmp_str):
	izd_val = float(tmp_str)
else:
	print("Издержки-не число")
	exit()
	
if vir_val>izd_val:
	print("Прибыль!")
	person = input("Количество работников\n")
	if is_digit(person):
		print("Выручка на работника=", (vir_val-izd_val)/int(person))
	else:
		print("Количество работников - не число")
		exit()
elif vir_val<izd_val:
	print("Убыток!")
else:
	print("Выживание!")
