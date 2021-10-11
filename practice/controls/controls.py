import math


def transpose(a):
    """Транспозиция матрицы"""
    b = []
    for i in range(len(a[0])):
        b.append([])
        for j in range(len(a)):
            b[i].append(a[j][i])
    return b
    pass


def read_lines(input, print):
    """Количество непустых строк во вводе до первой пустой"""
    sums = 0
    while True:
        d = input()
        if d == '':
            break
        else:
            sums += 1
    print(sums)
    pass


def min_prime(n):
    """Минимальный простой делитель числа"""
    for i in range(2, n + 1):
        if n % i == 0:
            return i
    pass


def from_hexadecimal(s):
    """Перевод из шестнадцатеричной системы счисления"""
    b = list()
    s1 = list()
    for o in range(len(s)):
        s1.append(s[o])
    # print(s1)
    for i in s1:
        if i == 'A':
            i = 10
        elif i == 'B':
            i = 11
        elif i == 'C':
            i = 12
        elif i == 'D':
            i = 13
        elif i == 'E':
            i = 14
        elif i == 'F':
            i = 15
        i = int(i)
        b.append(i)
    sums = 0
    c = b[::-1]
    # print(c)
    for j in range(0, len(c)):
        sums = c[j] * (16) ** j + sums
    # print(sums)
    return sums
    pass
