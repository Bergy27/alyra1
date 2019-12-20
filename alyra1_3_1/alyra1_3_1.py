def chiffreCesar(str, decallage):
	res = ""
	for c in str:
		toInt = (ord(c)+decallage)%127
		if toInt<34:
			res+=chr(toInt+33)
		else:
			res+=chr(toInt)
	return res

print(chiffreCesar("abc", 1))
print(chiffreCesar("sjdfbks|fgdsagHBZASVZ}~", 2))
