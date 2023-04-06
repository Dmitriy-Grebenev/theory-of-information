import random
from math import ceil
from decimal import Decimal

FIELD_SIZE = 10**5


def reconstruct_secret(shares):
	"""
	Объединяет отдельные доли (точки на графике)
	используя интерполяцию Лагранжа.

	`shares` - это список точек (x, y), принадлежащих
	полиному с константой нашего ключа.
	"""
	sums = 0
	prod_arr = []

	for j, share_j in enumerate(shares):
		xj, yj = share_j
		prod = Decimal(1)

		for i, share_i in enumerate(shares):
			xi, _ = share_i
			if i != j:
				prod *= Decimal(Decimal(xi)/(xi-xj))

		prod *= yj
		sums += Decimal(prod)

	return int(round(Decimal(sums), 0))


def polynom(x, coefficients):
	"""
	Эта функция генерирует одну точку на графике заданного полинома
	в `x`. Полином задается списком `коэффициентов`.
	"""
	point = 0
	# Перебираем обратный список, чтобы индексы из enumerate совпадали с индексами коэффициентов.
	# фактическим индексам коэффициентов
	for coefficient_index, coefficient_value in enumerate(coefficients[::-1]):
		point += x ** coefficient_index * coefficient_value
	return point


def coeff(t, secret):
	"""
	Случайным образом генерируем список коэффициентов для многочлена со
	степенью `t` - 1, константой которого является `secret`.

	Например, с коэффициентом 3-й степени следующим образом:
		3x^3 + 4x^2 + 18x + 554

		554 - это секрет, а степень полинома + 1 - это
		сколько точек необходимо для восстановления этого секрета.
		(в данном случае это 4 точки).
	"""
	coeff = [random.randrange(0, FIELD_SIZE) for _ in range(t - 1)]
	coeff.append(secret)
	return coeff


def generate_shares(n, m, secret):
	"""
	Разделить данный `секрет` на `n` долей с минимальным порогом
	`m` долей для восстановления этого `секрета`, используя алгоритм SSS.
	"""
	coefficients = coeff(m, secret)
	shares = []

	for i in range(1, n+1):
		x = random.randrange(1, FIELD_SIZE)
		shares.append((x, polynom(x, coefficients)))

	return shares


if __name__ == '__main__':

	# (3,5) схема разделения
	t, n = 3, 5
	secret = 1234
	print(f'Исходный секрет: {secret}')

	# Фаза I: генерация долей
	shares = generate_shares(n, t, secret)
	print(f'Доли секрета: {", ".join(str(share) for share in shares)}')

	# Фаза II: Восстановление секрета
	# Выбираем t долей случайным образом для
	# реконструкции
	pool = random.sample(shares, t)
	print(f'Объединение долей: {", ".join(str(share) for share in pool)}')
	print(f'Восстановленный секрет: {reconstruct_secret(pool)}')
