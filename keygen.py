import random
import sympy
import sys

p = 0
q = 0

#Generate a random number and test for primality
#Repeat until a prime number is found
def generate_prime():
    prime = 0
    attempt = 0
    while not sympy.isprime(prime):
        attempt += 1
        prime = random.getrandbits(500)
        sys.stdout.write("\r" + "Attempt: " + str(attempt))
        sys.stdout.flush()
    return prime

p = generate_prime()
q = generate_prime()
phi_n = (p - 1) * (q - 1)
n = p * q
e = 65537

 

print("\n" + "p = " + str(p))
print("q = " + str(q))
print(e)
