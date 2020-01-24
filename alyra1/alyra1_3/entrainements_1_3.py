MAJ = 65

def frequences(text):
	results = {}
	for l in text:
		if l in results:
			results[l] += 1
		else:
			results[l] = 1
	return results

def regroupement(text, n):
	text = text.upper().replace(" ","")
	res = [""]*n
	for index, t in enumerate(text):
		res[index%n] += t
	return res


def vigenere(keyword, text, method):
	length = len(keyword)
	res = ""
	if method=="encrypt":
		for index, t in enumerate(text):
			res += chr((((ord(t)-MAJ)+(ord(keyword[index%length])-MAJ))%26)+65)
		return res
	elif method=="decrypt":
		for index, t in enumerate(text):
			res += chr((((ord(t)-MAJ)-(ord(keyword[index%length])-MAJ))%26)+65)
		return res
	else:
		return None


#Entrainement A et B
message = "VOICIUNMESSAGE"
key = "ABC"
encrypt = vigenere(key, message, "encrypt")
decrypt = vigenere(key, encrypt, "decrypt")
print(encrypt)
print(decrypt)

#Entrainement C
print(regroupement("Mes vieilles tantes", 3))

#Entrainement D
text="PVADGHFLSHPJNPLUVAGXVVRBRUKCGXEVQINPVBXLVZLRMKFLSXEZQXOGCCHXEICIXUKSCXKEDDKORRXHPHSXGGJRRHPESTJWVBTJWVJFNGJSCLQLBJGUVSATNRJXFKKCBTKJOJXEVJJBQLATNZHSXECUCIBGELTGVGCJOGERPMQLRBHOVLIKGMCAXTCCHXEICIXUKYRVGJQXUNVYIHWJATLVSGTGRFSGJWFGXEARSCITFZAXOVBJLGTPTMEVOJBHRGIITFZAXOVBPGUCCHXEICIVGJRFNKCNTNVVRGXFZTJEILCIKCYGGXXVJTHGUGEXHZLXMRRPSXEYGUYTVPAXPZEBXFLQEAKEVHBXFSHOQLJTSRVPRXTCCHLGTPTMUTCHMNRRPVJVBTECIYXLQECCNPJCCLEVQIECKYRAGUCATRYGAHUFNWBGRSRHPKPPBTVJTFAJRTKGVQIICIBTYKEGIBQEBJGCLRGXQIBGXSLCAXRIMQEGDCXEGJRXGCTATLUZZAXCCYGTKJMCWCEQAXUDWHMGICHWGCYCMKHSXMGJCJEUUCGTTVQXGKKGTLRRPKBGELTGVRJPVQDNGXJVLHBQEBJFAJRTKGVRAXEYPXLVZYCBUDCTLVSCPNEFSEINLQGTFZAPEGEADKGCCBRUKCGXGJRRXSLGTLVRZHHNLKTGVZLPVEVQHBDCCPECIYXLQERWHORQSTSLGCEGGJJLIIYCWVYCDEQXGTGFVRDNVVJPVJICIBGERTFGUGTOCCCTMNRPTYGICCVGVLRHTVYJCQLPSAWZBTMQLRTECKFTHNFEXXEYPTMKVLCXKEQXLVVQJKNVDPBVHSTECIYIBQEYABVVQPKTVRTTWJCJBNUSBRUKCGXNVKNLVVPTXUKQPVTVQXOQLQEKGWCGXBZJTLVKPPGUTCCWCERXEGJRSBXZLPEQIQFNGCCHXEICIXUKNGHHRLTEGJCRKGKCHMKDKPGGERPECTMCWKKGDGJLKPBPVGAXUKFJFCZLTMEVQIIQLPFNQZDXWGCCPLCMMRTVZMCECGPDUNVKPMKJYIBQEJPKGWJTQKFLEAKCMHHRYGFNGZLIXTIMVXNVQTVTVRXGVVPGHIVJWNORLXMGUSHXEICILKTCITKKSCFAJRTKGVJAXPVJXGVVPGHIVPPBVGYHEGDWHMGICCXUKNPLWECRTVVEDKKVNWBNFQDIJZOJX"
#On essaye pour une clé de 1, 2, 3, 4 ou 5 caractères
for i in range(1, 6):
	print("Clé de longueur : "+str(i))
	groups = regroupement(text, i)
	key = ""
	#On regroupe le texte par caractère d'encryption
	for group in groups:
		#On compte la fréquence de chaque caractère encryptée
		freq = frequences(group)
		freq_sorted = {k: v for k, v in sorted(freq.items(), reverse=True, key=lambda item: item[1])}
		plain = "E"
		cipher = list(freq_sorted.keys())[0]
		#On calcule la différence entre le caractère qui a la plus grande fréquence (cipher) et le "E" qui est le caractère le plus présent dans la langue française
		#On trouve théoriquement le caractère qui a permis l'encryption	
		key+=chr(((ord(cipher)-ord(plain))%26)+65)
	print(key)
	#On teste la clé qu'on a trouvé
	print(vigenere(key, text, "decrypt"))






