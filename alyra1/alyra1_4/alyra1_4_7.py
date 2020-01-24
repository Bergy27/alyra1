#scriptPubKey: OP_DUP OP_HASH160 hashCléPub OP_EQUALVERIFY OP_CHECKSIG

#signature cléPub OP_DUP OP_HASH160 hashCléPub OP_EQUALVERIFY OP_CHECKSIG
#signature --> ajoute la signature en haut de la pile
#cléPub --> ajoute la clé publique en haut de la pile
#OP_DUP --> duplique la dernière valeur de la pile
#OP_HASH160 --> effectue le double hash de la dernière valeur et le place dans la pile
#hashCléPub --> ajoute ce hash attendu dans la pile
#OP_EQUALVERIFY --> vérifie que les deux valeurs précédentes sont égales
#OP_CHECKSIG  --> vérifie que la signature correspond bien à clé publique fournie et au hash de la transaction.

import hashlib
import binascii

def op_equalverify(pile):
	if pile[-1]==pile[-2]:
		return True
	else:
		return False

def op_hash160(pile):
	sha256 = hashlib.sha256(binascii.unhexlify(pile[-1])).hexdigest()
	ripemd160 = hashlib.new('ripemd160')
	ripemd160.update(binascii.unhexlify(sha256))
	hash160 = ripemd160.hexdigest()
	pile = pop(pile)
	return push(hash160, pile)

def op_dup(pile):
	pile.append(pile[-1])
	return pile

def push(element, pile):
	pile.append(element)
	return pile

def pop(pile):
	return pile[:-1]


def parseScriptSig(scriptSig):
	#remove 0x
	scriptSig = scriptSig[2:]

	#init result
	parsingScritSig = []

	#start at index 0	
	cursor = 0

	#when cursor finish, we return the parsing
	while cursor<len(scriptSig):
		varIntInDec = int(scriptSig[cursor:cursor+2], 16)
		parsingScritSig.append(scriptSig[cursor+2:varIntInDec*2+cursor+2])
		cursor = varIntInDec*2+cursor+2

	return [parsingScritSig[0], parsingScritSig[1]]



def verificationP2PKH(scriptSig, scriptPubSig):
	pile = []
	signature, clePub = parseScriptSig(scriptSig)
	pile = push(signature, pile)
	pile = push(clePub, pile)

	cursor = 2
	instructions =  False
	varInt = False
	while cursor<len(scriptPubSig):
		print("\tpile : "+str(pile))
		if varInt:
			varIntDec = int(scriptPubSig[cursor:cursor+2], 16)
			pile = push(scriptPubSig[cursor+2:cursor+2+varIntDec*2], pile)
			print("Ajout de la valeur du hash de la clé publique sur la pile")
			print("\tpile : "+str(pile))
			cursor = cursor+2+varIntDec*2
			varInt=False


		if scriptPubSig[cursor:cursor+2] in ["00", "51", "76", "93", "88", "a9", "ac", "b1"]:
			instructions = True
		else:
			instructions = False
		if instructions:
			if scriptPubSig[cursor:cursor+2]=="76":
				print("Duplique l’item en haut de la pile")
				pile = op_dup(pile)
			elif scriptPubSig[cursor:cursor+2]=="a9":
				print("Effectue un SHA-256 puis un RIPEMD-160 sur l’élément en haut de la pile")
				pile = op_hash160(pile)
			elif scriptPubSig[cursor:cursor+2]=="88":
				print("Retourne vrai si les deux premiers éléments de la pile sont égaux (bit à bit) et puis dépile cette valeur si elle est vraie. Sinon le script termine avec une erreur (la transaction est donc invalide)")
				if op_equalverify(pile):
					pile = pop(pile)
				else:
					return False
			elif scriptPubSig[cursor:cursor+2]=="ac":
				print("Prend en paramètre une signature et une clé publique. Hash160 de l’ensemble de la transaction, puis vérifie que la signature correspond bien à la signature de ce hash par la clé publique")
				print("Toujours vrai")
				return True
				#...
			

			cursor+=2
		else:
			varInt = True


if verificationP2PKH("0x483045022100d544eb1ede691f9833d44e5266e923dae058f702d2891e4ee87621a433ccdf4f022021e405c26b0483cd7c5636e4127a9510f3184d1994015aae43a228faa608362001210372cc7efb1961962bba20db0c6a3eebdde0ae606986bf76cb863fa460aee8475c", "0x76a9147c3f2e0e3f3ec87981f9f2059537a355db03f9e888ac"):
	print("La transaction est valide")
else:
	print("La transaction n'est pas valide")