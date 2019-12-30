import sys
import random

def egcd(b, n):
    (x0, x1, y0, y1) = (1, 0, 0, 1)
    while n != 0:
        (q, b, n) = (b // n, n, b % n)
        (x0, x1) = (x1, x0 - q * x1)
        (y0, y1) = (y1, y0 - q * y1)
    return (b, x0, y0)

def getPrimes(maximum):
	res = []
	for i in range(3, maximum-1):
		if isPrime(i):
			res += [i]
	return res


def isPrime(number):
	for i in range(2,number):
		if number%i==0:
			return False
	return True

p = int(sys.argv[1])
q = int(sys.argv[2])


if isPrime(p) and isPrime(q):
	n = p*q
	print("n : "+str(n))
	indicatrice_euler = (p-1)*(q-1)
	print("indicatrice_euler : "+str(indicatrice_euler))

	list_of_primes = getPrimes(indicatrice_euler)
	c = random.choice(list_of_primes)
	print("c : "+str(c))

	(_, d, k) = egcd(c, indicatrice_euler)
	print("d : "+str(d))
	print("k : "+str(k))

	print("cd mod(indicatrice_euler) : "+str((c*d)%indicatrice_euler))
	print("cd + k(indicatrice_euler) : "+str(c*d+k*indicatrice_euler))