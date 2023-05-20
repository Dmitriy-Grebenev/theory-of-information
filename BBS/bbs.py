import random

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

def generate_blum_sequence(L):
    """Генерация псевдослучайной последовательности по методу Блюма"""
    p = 0
    q = 0

    # Находим простые числа p и q
    while not (is_prime(p) and is_prime(q)):
        u = random.randint(1, 1e6)
        v = random.randint(1, 1e6)
        p = 4 * u + 3
        q = 4 * v + 3

    n = p * q  # Число Блюма

    s = random.randint(2, n - 1)
    while s % n == 0:  # Убеждаемся, что s взаимнопростое с n
        s = random.randint(2, n - 1)

    x_0 = pow(s, 2, n)  # Начальное значение генератора

    blum_sequence = ""
    for _ in range(L):
        x_i = pow(x_0, 2, n)  # Вычисляем следующее значение x_i
        bit = x_i % 2  # Бит последовательности
        blum_sequence += str(bit)
        x_0 = x_i

    return blum_sequence

# Пример использования
L = 8  # Длина псевдослучайной последовательности
sequence = generate_blum_sequence(L)
print(sequence)
print(int(sequence, 2))
