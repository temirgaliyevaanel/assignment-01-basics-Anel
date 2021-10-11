import math


def triangle(a, b, c):
    """Проверка правила треугольника"""
    if min(a, b, c) > 0:
        if a < b + c and b < a + c and c < a + b:
            return True
        else:
            return False
    else:
        return False
    pass


def divide(n, k):
    """Разбиение на равные части"""
    a = n // k
    return a * k

    pass


def add_float(x, y):
    """Сложение не более, чем десятичных, дробных чисел"""
    x = float(x)
    y = float(y)
    return round((x + y), 1)
    pass


def distance(x1, x2):
    """Расстояние между точками"""
    a = abs(x1 - x2)
    return a

    pass


def compare_power(x1, d1, x2, d2):
    """Сравнение степеней"""
    a = x1 ** d1
    b = x2 ** d2
    if a < b:
        return -1
    elif a == b:
        return 0
    else:
        return 1
    pass
