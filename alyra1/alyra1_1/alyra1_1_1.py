import random

random_number = random.randint(1, 100)
print(random_number)
response = int(input("Devinez un nombre entre 1 et 100\n"))

if response==random_number:
	print("Du permier coup, c'est exact !")

while response!=random_number:
	diff = random_number-response
	if diff>0:
		value = "plus"
	elif diff<0:
		value = "moins"
	else:
		print("Exact !")
	if abs(diff)<=5:
		response = int(input("C'est un tout petit peu {}\n".format(value)))
	elif abs(diff)<=10:
		response = int(input("C'est un peu {}\n".format(value)))
	else:
		response = int(input("C'est beaucoup {}\n".format(value)))
		