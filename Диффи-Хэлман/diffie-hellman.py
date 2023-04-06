from random import randint

def generate_prime_number():
    # Генерируем случайное простое число
    prime_number = randint(100, 1000)
    while not is_prime_number(prime_number):
        prime_number += 1
    return prime_number

def is_prime_number(number):
    # Проверяем, является ли число простым
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def generate_primitive_root(prime_number):
    # Генерируем первообразный корень для заданного простого числа
    phi = prime_number - 1
    for i in range(2, phi):
        if gcd(i, phi) == 1:
            return i
    return None

def gcd(a, b):
    # Вычисляем наибольший общий делитель для двух чисел
    while b != 0:
        a, b = b, a % b
    return a

def diffie_hellman():
    # Генерируем простое число и первообразный корень
    prime_number = generate_prime_number()
    primitive_root = generate_primitive_root(prime_number)
    print(f"Prime number: {prime_number}")
    print(f"Primitive root: {primitive_root}")

    # Генерируем секретный ключ для Алисы и Боба
    alice_secret_key = randint(1, prime_number - 1)
    bob_secret_key = randint(1, prime_number - 1)

    # Вычисляем открытый ключ для Алисы и Боба
    alice_public_key = pow(primitive_root, alice_secret_key, prime_number)
    bob_public_key = pow(primitive_root, bob_secret_key, prime_number)

    # Вычисляем общий секретный ключ для Алисы и Боба
    alice_shared_secret = pow(bob_public_key, alice_secret_key, prime_number)
    bob_shared_secret = pow(alice_public_key, bob_secret_key, prime_number)

    # Проверяем, что общие секретные ключи совпадают
    assert alice_shared_secret == bob_shared_secret

    # Возвращаем общий секретный ключ
    return alice_shared_secret

shared_secret = diffie_hellman()
print(f"Shared secret: {shared_secret}")
