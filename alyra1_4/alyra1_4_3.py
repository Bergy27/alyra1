entree = "941e985075825e09de53b08cdd346bb67075ef0ce5c94f98853292d4bf94c10d010000006b483045022100ab44ef425e6d85c03cf301bc16465e3176b55bba9727706819eaf07cf84cf52d02203f7dc7ae9ab36bead14dd3c83c8c030bf8ce596e692021b66441b39b4b35e64e012102f63ae3eba460a8ed1be568b0c9a6c947abe9f079bcf861a7fdb2fd577ed48a81Feffffff"


print("Transaction passée : "+entree[0:64])
octet = [entree[0:64][i:i+2] for i in range(0, len(entree[0:64]), 2)]
octet.reverse()
print("Transaction passée (bon ordre) : "+"".join(octet))


print("Index de la sortie : "+entree[64:64+8])

varIntScriptSig = entree[64+8:64+8+2]
varIntSignature = entree[64+8+2:64+8+2+2]
varIntSignatureToDec = int(varIntSignature,16)
print("VarInt ScriptSig : "+varIntScriptSig)
print("VarInt Signature : "+varIntSignature)
print("Signature : "+entree[64+8+2+2:64+8+2+2+varIntSignatureToDec*2])
varIntClePublique = entree[64+8+2+2+varIntSignatureToDec*2:64+8+2+2+varIntSignatureToDec*2+2]
varIntClePubliqueToDec = int(varIntClePublique, 16)
print("VarInt Clé publique : "+varIntClePublique)
print("Clé publique : "+entree[64+8+2+2+varIntSignatureToDec*2+2:64+8+2+2+varIntSignatureToDec*2+2+varIntClePubliqueToDec*2])
print("Séquence : "+entree[-8:])