import random
import math

# Функция для проверки, является ли число простым
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Функция для поиска простых чисел в заданном диапазоне
def get_primes(start, stop):
    primes = []
    for num in range(start, stop):
        if is_prime(num):
            primes.append(num)
    return primes

# Функция для генерации ключей RSA
def generate_keys(p, q):
    # Вычисляем модуль и функцию Эйлера
    n = p * q
    phi = (p - 1) * (q - 1)

    # Выбираем случайное целое число e, взаимно простое с phi
    e = random.randrange(1, phi)
    while math.gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Вычисляем мультипликативную инверсию e по модулю phi
    d = pow(e, -1, phi)

    # Возвращаем открытый и закрытый ключи
    return ((e, n), (d, n))

# Функция для шифрования сообщения с помощью открытого ключа
def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(c), e, n) for c in message]
    return encrypted_message

# Функция для расшифрования сообщения с помощью закрытого ключа
def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = [chr(pow(c, d, n)) for c in encrypted_message]
    return ''.join(decrypted_message)

# Пример использования
primes = get_primes(100, 1000)
p, q = random.sample(primes, 2)
public_key, private_key = generate_keys(p, q)
message = "Hello, World!"
encrypted_message = encrypt(message, public_key)
decrypted_message = decrypt(encrypted_message, private_key)
print("Original message: ", message)
print("Encrypted message: ", encrypted_message)
print("Decrypted message: ", decrypted_message)
