import math
import random

def generate_prime(bits):
    """Генерация случайного простого числа с заданной битовой длиной"""
    while True:
        num = random.getrandbits(bits) | (1 << bits-1) | 1  # Генерируем нечетное число
        if is_prime(num):
            return num

def is_prime(n, k=10):
    """Проверка, является ли число простым"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = 0
    s = n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def jacobi_symbol(a, n):
    """Вычисление символа Якоби"""
    if n <= 0 or n % 2 == 0:
        raise ValueError("n должно быть нечетным положительным числом.")
    a = a % n
    t = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            t = -t
        a %= n
    if n == 1:
        return t
    else:
        return 0

def generate_bbs(bits):
    """Генерация последовательности псевдослучайных чисел методом BBS"""
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    seed = random.randint(1, n - 1)
    sequence = ""
    for _ in range(bits):
        seed = pow(seed, 2, n)
        bit = seed % 2
        sequence += str(bit)
    return sequence

# Пример использования
bits = 64
random_sequence = generate_bbs(bits)
print("В двоичной системе счисления: \n", random_sequence)
print("В десятичной системе счисления: \n", int(random_sequence, 2))
