import random

private_key = random.randint(0,2**16)

a = 0
b = 7
G = "0279BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798"
n = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141"

public_key = (private_key*int(G,16))%int(n,16)
print("private key : "+str(private_key))
print("public key : "+str(public_key))
