import sys

HEX = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e"]

def conversion(number, hex):
	res = number//16
	remainder = number%16
	if number//16==0:
		if len(hex)%2==0:
			hex += HEX[remainder]+"0"
		else:
			hex += HEX[remainder]
		octet = [hex[i:i+2] for i in range(0, len(hex), 2)]
		return "0x "+" ".join(list(map(lambda element : element[::-1], octet))[::-1]), "0x "+" ".join(list(map(lambda element : element[::-1], octet)))
	else:
		return conversion(res, hex+HEX[remainder])


print(conversion(int(sys.argv[1]), ""))