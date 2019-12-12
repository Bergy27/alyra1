import hashlib 

serveurs = [
	["Amsterdam", "153.8.223.72"],
	["Chennai", "169.38.84.49"],
	["Dallas", "169.46.49.112"],
	["Dallas, TX, USA", "184.173.213.155"],
	["Frankfurt", "159.122.100.41"],
	["Hong Kong", "119.81.134.212"],
	["London", "5.10.5.200"],
	["London", "158.176.81.249"],
	["Melbourne", "168.1.168.251"],
	["Mexico City", "169.57.7.230"],
	["Milan", "159.122.142.111"],
	["Paris", "159.8.78.42"],
	["San Jose", "192.155.217.197"],
	["São Paulo", "169.57.163.228"],
	["Toronto", "169.56.184.72"],
	["Washington DC", "50.87.60.166"],
]

def search(data, hashTable):
	sha1 = hashlib.sha1(data.encode()).hexdigest()
	return help_search(sha1, 0, hashTable)


def help_search(sha1, index, hashTable):
	key = sha1[index]
	if key=="0" or key == "1":
		if isinstance(hashTable[0], tuple):
			return hashTable[0][0]
		else:
			return help_search(sha1, index+1, hashTable[0])
	if key=="2" or key == "3":
		if isinstance(hashTable[1], tuple):
			return hashTable[1][0]
		else:
			return help_search(sha1, index+1, hashTable[1])
	if key=="4" or key == "5":
		if isinstance(hashTable[2], tuple):
			return hashTable[2][0]
		else:
			return help_search(sha1, index+1, hashTable[2])
	if key=="6" or key == "7":
		if isinstance(hashTable[3], tuple):
			return hashTable[3][0]
		else:
			return help_search(sha1, index+1, hashTable[3])
	if key=="8" or key == "9":
		if isinstance(hashTable[4], tuple):
			return hashTable[4][0]
		else:
			return help_search(sha1, index+1, hashTable[4])
	if key=="a" or key == "b":
		if isinstance(hashTable[5], tuple):
			return hashTable[5][0]
		else:
			return help_search(sha1, index+1, hashTable[5])
	if key=="c" or key == "d":
		if isinstance(hashTable[6], tuple):
			return hashTable[6][0]
		else:
			return help_search(sha1, index+1, hashTable[6])
	if key=="e" or key=="f":
		if isinstance(hashTable[7], tuple):
			return hashTable[7][0]
		else:
			return help_search(sha1, index+1, hashTable[7])


def coll(index, result, hashTable, data, indexTab):
	if hashTable[indexTab] is None:
		hashTable[indexTab] = (data, result)
	elif isinstance(hashTable[indexTab], tuple):
		tmpData, tmpResult = hashTable[indexTab]
		hashTable[indexTab] = [None]*8
		store(index+1, tmpResult, hashTable[indexTab], tmpData)
		store(index+1, result, hashTable[indexTab], data)
	else:
		store(index+1, result, hashTable[indexTab], data)


def store(index, result, hashTable, data):
	key = result[index]
	if key=="0" or key=="1":
		coll(index, result, hashTable, data, 0)
	if key=="2" or key=="3":
		coll(index, result, hashTable, data, 1)
	if key=="4" or key=="5":
		coll(index, result, hashTable, data, 2)
	if key=="6" or key=="7":
		coll(index, result, hashTable, data, 3)
	if key=="8" or key=="9":
		coll(index, result, hashTable, data, 4)
	if key=="a" or key=="b":
		coll(index, result, hashTable, data, 5)
	if key=="c" or key=="d":
		coll(index, result, hashTable, data, 6)
	if key=="e" or key=="f":
		coll(index, result, hashTable, data, 7)
	return hashTable

hashTable = [None]*8
for serveur in serveurs:
	result = hashlib.sha1(serveur[1].encode()).hexdigest()
	hashTable = store(0, result, hashTable, serveur[0])

print(hashTable)

for serveur in serveurs:
	print(search(serveur[1], hashTable))
