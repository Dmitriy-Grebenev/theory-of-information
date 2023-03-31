import math

def encrypt(key, message):
    # Имитирует столбцы в матрице с помощью массива строк.
    ciphertext = [''] * key
    # Итерации по каждому столбцу в шифротексте.
    for column in range(key):
        index = column
        # Итерация до конца открытого текста.
        while index < len(message):
            # Помещает символ в конец столбца:
            ciphertext[column] += message[index]
            # Перемещает индекс на следующий символ.
            index += key

    # Возвращает массив ciphertext как одну строку.
    return ''.join(ciphertext)


def decrypt(key, message):
    # Вычисляет размерность матрицы: сколько строк и столбцов.
    # - нам это нужно для отслеживания положения.
    nrows = key
    ncols = math.ceil(len(message) / key)

    # Подсчитывает количество пустых позиций в матрице благодаря
    # функции ceil().
    empty_positions = nrows * ncols - len(message)

    # Имитирует столбцы в матрице с помощью массива строк.
    plaintext = [''] * ncols

    # Инициализирует переменные отслеживания позиций.
    column = 0
    row = 0

    # Итерация по каждому символу в шифрованном сообщении.
    for symbol in message:
        # Заполняет матрицу в порядке перемещения строки за строкой.
        plaintext[column] += symbol
        column += 1

        # В случае, если мы находимся после последнего столбца...
        # ... или в позиции, которая должна быть пустой - такие позиции
        # возможны только в последнем столбце - оберните к началу следующей строки.
        if column == ncols or (column == ncols - 1 and row >= nrows - empty_positions):
            column = 0
            row += 1

    # Возвращает массив plaintext в виде одной строки.
    return ''.join(plaintext)


message = 'Here is our first message!'
key = 2
ciphertext = encrypt(key, message)
# Разграничивает шифротекст для целей отображения, т.е. показывает
# символ <пробела>, если он есть в конце.
print(f'Ciphertext: {ciphertext}')
# Печатает открытый текст для проверки правильности алгоритма.
plaintext = decrypt(key, ciphertext)
print(f'Plaintext: {plaintext}')
