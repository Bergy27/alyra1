entree = "01000000x01f129de033c57582efb464e94ad438fff493cc4de4481729b85971236858275c2010000006a4730440220155a2ea4a702cadf37052c87bfe46f0bd24809759acff8d8a7206979610e46f6022052b688b784fa1dcb1cffeef89e7486344b814b0c578133a7b0bce5be978a9208012103915170b588170cbcf6380ef701d19bd18a526611c0c69c62d2c29ff6863d501affffffff02ccaec817000000001976a9142527ce7f0300330012d6f97672d9acb5130ec4f888ac18411a000000000017a9140b8372dffcb39943c7bfca84f9c40763b8fa9a068700000000"
print(len(entree))
print("Version : "+entree[0:8])

print("ENTREES")

print("Taille des entrées : "+entree[9:9+2])

print("Transaction passée : "+entree[9+2:9+2+64])
octet = [entree[9+2:9+2+64][i:i+2] for i in range(0, len(entree[9+2:9+2+64]), 2)]
octet.reverse()
print("Transaction passée (bon ordre) : "+"".join(octet))
print(len("".join(octet)))

print("Index de la sortie : "+entree[9+2+64:9+2+64+8])

varIntScriptSig = entree[9+2+64+8:9+2+64+8+2]
varIntSignature = entree[9+2+64+8+2:9+2+64+8+2+2]
varIntSignatureToDec = int(varIntSignature,16)
print("VarInt ScriptSig : "+varIntScriptSig)
print("VarInt Signature : "+varIntSignature)
print("Signature : "+entree[9+2+64+8+2+2:9+2+64+8+2+2+varIntSignatureToDec*2])
varIntClePublique = entree[9+2+64+8+2+2+varIntSignatureToDec*2:9+2+64+8+2+2+varIntSignatureToDec*2+2]
varIntClePubliqueToDec = int(varIntClePublique, 16)
print("VarInt Clé publique : "+varIntClePublique)
print("Clé publique : "+entree[64+8+2+2+varIntSignatureToDec*2+2:64+8+2+2+varIntSignatureToDec*2+2+varIntClePubliqueToDec*2])
print("Séquence : "+entree[64+8+2+2+varIntSignatureToDec*2+2+varIntClePubliqueToDec*2:64+8+2+2+varIntSignatureToDec*2+2+varIntClePubliqueToDec*2+8])


print("SORTIES")
print("Taille des sorties : "+entree[64+8+2+2+varIntSignatureToDec*2+2+varIntClePubliqueToDec*2+8:64+8+2+2+varIntSignatureToDec*2+2+varIntClePubliqueToDec*2+8+2])
satoshis = entree[64+8+2+2+varIntSignatureToDec*2+2+varIntClePubliqueToDec*2+8+2:64+8+2+2+varIntSignatureToDec*2+2+varIntClePubliqueToDec*2+8+2+16]
print(int(satoshis,16))
print("Montant (en satoshis) : "+entree[64+8+2+2+varIntSignatureToDec*2+2+varIntClePubliqueToDec*2+8+2:64+8+2+2+varIntSignatureToDec*2+2+varIntClePubliqueToDec*2+8+2+16])
varIntScript = entree[64+8+2+2+varIntSignatureToDec*2+2+varIntClePubliqueToDec*2+8+2+16:64+8+2+2+varIntSignatureToDec*2+2+varIntClePubliqueToDec*2+8+2+16+2]
varIntScriptToDec = int(varIntScript, 16)-2
print("ScriptPubKey : "+entree[64+8+2+2+varIntSignatureToDec*2+2+varIntClePubliqueToDec*2+8+2+16+2:64+8+2+2+varIntSignatureToDec*2+2+varIntClePubliqueToDec*2+8+2+16+varIntScriptToDec])

print("LOCKTIME : "+entree[-8:])
