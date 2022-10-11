import base64
from email import message


def is_prime_number(num):
    i = 2
    _is_prime_number = True
    while i**2 <= num:
        if num % i == 0:

            _is_prime_number = False
            break
        i += 1
    return _is_prime_number


def modular_multiplicative(e, fi):
    d = 1
    while ((e % fi) * (d % fi)) % fi != 1:
        d += 1
    return d


p, q = 20, 20
while not(is_prime_number(p) and is_prime_number(q)):
    p, q = input("Введите два простых числа: ").split()
    p = int(p)
    q = int(q)

n = p*q
fi = (p-1)*(q-1)
e = 7
d = modular_multiplicative(e, fi)

public_key = (e, n)
private_key = (d, n)
print(public_key, private_key)
m = 2
coded_message = (m**public_key[0]) % public_key[1]
decoding_message = (coded_message ** private_key[0]) % private_key[1]
print(m, coded_message, decoding_message)

# Task2
text = b"The leaping of one fish would never disturb the flow of the river"
print(txt := base64.b64encode(text))
print(base64.b64decode(txt))
