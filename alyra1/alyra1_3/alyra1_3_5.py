from Crypto.PublicKey import RSA 
from Crypto.Hash import SHA256
from Crypto.Hash import RIPEMD
import random
import binascii
import sys

# Copyright (C) 2011 Sam Rushing
# Copyright (C) 2013-2014 The python-bitcoinlib developers
#
# This file is part of python-bitcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.
#https://python-bitcoinlib.readthedocs.io/en/latest/_modules/bitcoin/base58.html
b58_digits = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
def encode58(b):
    """Encode bytes to a base58-encoded string"""

    # Convert big-endian bytes to integer
    n = int('0x0' + binascii.hexlify(b).decode('utf8'), 16)

    # Divide that integer into bas58
    res = []
    while n > 0:
        n, r = divmod(n, 58)
        res.append(b58_digits[r])
    res = ''.join(res[::-1])

    # Encode leading zeros as base58 zeros
    czero = b'\x00'
    if sys.version > '3':
        # In Python3 indexing a bytes returns numbers, not characters.
        czero = 0
    pad = 0
    for c in b:
        if c == czero:
            pad += 1
        else:
            break
    return b58_digits[0] * pad + res


def calculateAdresse(number):
	#Calculer le hash SHA 256 puis RIPEMD160 (voir librairies dans le cours), on appelle ce résultat hash160 	
	sha256 = SHA256.new()
	number_in_bytes = number.to_bytes(2,byteorder='big')
	sha256.update(number_in_bytes)
	hash160 = RIPEMD.new(sha256.digest())
	#print(hash160.digest())

	#4 premiers octets du sha256(sha256(0x00 + hash160))
	sha256_2 = SHA256.new()
	sha256_3 = SHA256.new()
	#0x00+hash160
	sha256_2.update(bytes(1)+hash160.digest())
	sha256_3.update(sha256_2.digest())
	#4 premiers octets			
	#print(sha256_3.digest()[:4])

	#Convertir le nombre en base 58	
	return encode58(bytes(1)+hash160.digest()+sha256_3.digest()[:4])



print(calculateAdresse(random.randint(0,2**16)))

