import random

def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None):
    """
        Генерирует список случайных целых чисел.

        Args:
            n (int): Требуемое количество элементов в списке.
            lo (int): Нижняя граница диапазона (включительно).
            hi (int): Верхняя граница диапазона (включительно).
            distinct (bool, optional): Если True, все элементы будут уникальными. По умолчанию False.
            seed (int, optional): Начальное значение для генератора случайных чисел
                для воспроизводимости результатов. По умолчанию None.

        Returns:
            list[int]: Список из n случайных целых чисел.
    """
    if seed is not None:
        random.seed(seed)
    if distinct:
        return random.sample(range(lo, hi), n)
    else:
        return [random.randint(lo, hi) for _ in range(n)]

def nearly_sorted(n: int, swaps: int, *, seed=None):
    """
        Генерирует список, который является "почти отсортированным".

        Список создается как полностью отсортированный (0, 1, 2, ..., n-1),
        после чего производится заданное количество случайных обменов (swaps).

        Args:
            n (int): Требуемое количество элементов (размер списка).
            swaps (int): Количество случайных обменов, которые нужно произвести.
            seed (int, optional): Начальное значение для генератора случайных чисел.

        Returns:
            list[int]: Почти отсортированный список.
    """
    if seed is not None:
        random.seed(seed)
    arr = list(range(n))
    for _ in range(swaps):
        i,j = random.randint(0,n-1), random.randint(0,n-1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr
def many_duplicates(n: int, k_unique=5, *, seed=None):
    """
        Генерирует список с заданным количеством повторяющихся значений.

        Args:
            n (int): Требуемое количество элементов.
            k_unique (int, optional): Количество уникальных значений, которые
                будут использоваться в списке. По умолчанию 5.
            seed (int, optional): Начальное значение для генератора случайных чисел.

        Returns:
            list[int]: Список с множеством дубликатов.
    """
    if seed is not None:
        random.seed(seed)
    choices = [random.randint(0,10000) for _ in range(k_unique)]
    return [random.choice(choices) for _ in range(n)]
def reverse_sorted(n: int):
    """
        Генерирует список, отсортированный в обратном порядке.

        Args:
            n (int): Требуемое количество элементов.

        Returns:
            list[int]: Список целых чисел от n до 1.
    """
    return list(range(n, 0, -1))
def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None):
    """
        Генерирует список случайных чисел с плавающей запятой (float).

        Args:
            n (int): Требуемое количество элементов.
            lo (float, optional): Нижняя граница диапазона (включительно). По умолчанию 0.0.
            hi (float, optional): Верхняя граница диапазона (невключительно). По умолчанию 1.0.
            seed (int, optional): Начальное значение для генератора случайных чисел.

        Returns:
            list[float]: Список из n случайных чисел с плавающей запятой.
    """
    if seed is not None:
        random.seed(seed)
    return [random.uniform(lo, hi) for _ in range(n)]
