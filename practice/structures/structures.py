def kth(a, k):
    """k-е по величине значение в массиве"""
    b = sorted(a)
    return b[k - 1]
    pass


def head_tail(a, k):
    """Первые и последние k элементов в массиве"""
    b = []
    for i in range(0, k):
        b.append(a[i])
    a = a[::-1]
    for i in range(0, k):
        b.insert(k, a[i])
    return b
    pass


def filter_sort(a, c):
    """Отсортировать копию массива, удалив строки с символом c"""
    return sorted([elem for elem in a if c not in elem])
    pass


def build_dict(keys, values):
    """Построить словарь по набору ключей и значений"""
    return dict(zip(keys, values))


def compare_contents(a1, a2):
    """Проверка наборов элементов на совпадение"""
    a = 0
    for i in a1:
        if i not in a2:
            return False
        else:
            a = 1
    for j in a2:
        if j not in a1:
            return False
    return True
    pass
