#0xfd 2 octets
#0xfe 4 octets
#0xff 8 octets

import sys

HEX = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

def conversionVarInt(number, hex):
	res = number//16
	remainder = number%16
	if number//16==0:
		if len(hex)%2==0:
			hex += HEX[remainder]+"0"
		else:
			hex += HEX[remainder]
		octet = [hex[i:i+2] for i in range(0, len(hex), 2)]
		octet = list(map(lambda element : element[::-1], octet))
		numberOctets = len(octet)
		if octet[0]=="fd" or octet[0]=="fe" or octet[0]=="ff":
			numberOctets += 1

		while len(octet)!=2**(numberOctets-1):
			octet.append("00")

		if numberOctets==2:
			return "0x fd "+" ".join(octet)
		elif numberOctets==3:
			return "0x fe "+" ".join(octet)
		elif numberOctets==4:
			return "0x ff "+" ".join(octet)
		return "0x "+" ".join(octet)
	else:
		return conversionVarInt(res, hex+HEX[remainder])


print(conversionVarInt(int(sys.argv[1]), ""))