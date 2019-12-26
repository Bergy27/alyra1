def frequences(text):
	results = {}
	for l in text:
		if l in results:
			results[l] += 1
		else:
			results[l] = 1
	return results



print(frequences("Etre contesté, c’est être constaté"))