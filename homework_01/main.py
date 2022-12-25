"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_even(x):
    return not x % 2


def filter_odd(x):
    return x % 2


def filter_prime(x):
    if x == 1:
        return False
    d = 2
    while x % d != 0:
        d += 1
    return d == x


def filter_numbers(number_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

   >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]

    """
    if filter_type == ODD:
        return list(filter(filter_odd, number_list))
    if filter_type == EVEN:
        return list(filter(filter_even, number_list))
    if filter_type == PRIME:
        return list(filter(filter_prime, number_list))

