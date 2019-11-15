def estPalindrome(string):
	string = string.replace(" ","")
	return string==string[::-1]

print(estPalindrome("ESOPE RESTE ICI ET SE REPOSE"))
print(estPalindrome("ASSIETTE"))
