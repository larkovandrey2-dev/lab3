from typing import TypeVar, Callable, Any

T = TypeVar('T')


def bubble_sort(a: list[T], key: Callable[[T], Any] | None = None,
                cmp: Callable[[Any, Any], int] | None = None) -> list[T]:
    """
        Сортировка пузырьком (Bubble Sort).
        Проходит по списку многократно, сравнивая соседние элементы и меняя их местами,
        если они стоят в неправильном порядке.

        Args:
            a (list[T]): Список для сортировки.
            key (Callable, optional): Функция для извлечения ключа сравнения из элемента.
            cmp (Callable, optional): Функция сравнения двух ключей (возвращает -1, 0, 1).

        Returns:
            list[T]: Отсортированный список.
    """
    if key is None:
        def identity(x):
            return x

        key = identity
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            x,y = key(a[j]),key(a[j + 1])
            if cmp:
                if cmp(x,y) > 0:
                    a[j], a[j + 1] = a[j + 1], a[j]
            else:
                if x > y:
                    a[j], a[j + 1] = a[j + 1], a[j]
    return a

def quick_sort(a: list[T], key: Callable[[T], Any] | None = None,
               cmp: Callable[[Any, Any], int] | None = None) -> list[T]:
    """
        Быстрая сортировка (Quick Sort).
        Выбирает опорный элемент,
        разделяет массив на три части (меньше, равно, больше опорного) и рекурсивно сортирует их.

        Args:
            a (list[T]): Исходный список.
            key (Callable, optional): Функция для извлечения ключа сравнения.
            cmp (Callable, optional): Функция сравнения.

        Returns:
            list[T]: Новый отсортированный список.
        """
    n = len(a)
    if key is None:
        def identity(x):
            return x

        key = identity

    if n <= 1:
        return a
    pivot = a[n//2]
    pivot_key = key(pivot)
    left,right,middle = [],[],[]
    for x in a:
        x_key = key(x)
        if cmp:
            if cmp(x_key, pivot_key) < 0:
                left.append(x)
            elif cmp(x_key, pivot_key) > 0:
                right.append(x)
            else:
                middle.append(x)
        else:
            if x_key < pivot_key:
                left.append(x)
            elif x_key > pivot_key:
                right.append(x)
            else:
                middle.append(x)
    return quick_sort(left, key, cmp) + middle + quick_sort(right, key, cmp)
def merge_sort(a: list[T], key: Callable[[T], Any] | None = None,
               cmp: Callable[[Any, Any], int] | None = None) -> list[T]:
    """
        Сортировка слиянием (Merge Sort).
        Рекурсивно делит список пополам до единичных элементов, а затем собирает
        их обратно в отсортированном порядке.

        Args:
            a (list[T]): Исходный список.
            key (Callable, optional): Функция ключа.
            cmp (Callable, optional): Функция сравнения.

        Returns:
            list[T]: Новый отсортированный список.
    """
    n = len(a)
    if key is None:
        def identity(x):
            return x

        key = identity

    if n <= 1:
        return a
    mid = n//2
    left = merge_sort(a[:mid],key,cmp)
    right = merge_sort(a[mid:],key,cmp)
    return merge(left,right,key,cmp)
def merge(left, right, key, cmp):
    """
        Вспомогательная функция для слияния двух отсортированных списков.

        Args:
            left (list): Левая часть списка.
            right (list): Правая часть списка.
            key (Callable): Функция ключа.
            cmp (Callable, optional): Функция сравнения.

        Returns:
            list: Объединенный отсортированный список.
        """
    sorted_l = []
    i = j = 0
    while i < len(left) and j < len(right):
        x, y = key(left[i]), key(right[j])
        if cmp:
            if cmp(x, y) <= 0:
                sorted_l.append(left[i])
                i += 1
            else:
                sorted_l.append(right[j])
                j += 1
        else:
            if x <= y:
                sorted_l.append(left[i])
                i += 1
            else:
                sorted_l.append(right[j])
                j += 1
    sorted_l += left[i:]
    sorted_l += right[j:]
    return sorted_l

def count_sort(a: list[int]) -> list[int]:
    """
        Сортировка подсчетом (Counting Sort).
        Работает только с целыми числами. Подсчитывает вхождения каждого числа
        и восстанавливает список.

        Args:
            a (list[int]): Список целых чисел.

        Returns:
            list[int]: Новый отсортированный список.
    """
    mn = min(a)
    mx = max(a)
    count: dict = {i: 0 for i in range(mn, mx+1)}
    sorted_l = []
    for x in a:
        count[x] += 1
    for i in range(mn, mx + 1):
        sorted_l += [i]*count[i]
    return sorted_l

def radix_sort(a: list[int], base:int = 10) -> list[int]:
    """
        Поразрядная сортировка (Radix Sort).
        Сортирует числа, обрабатывая разряды от младшего к старшему.
        Поддерживает отрицательные числа.

        Args:
            a (list[int]): Список целых чисел.
            base (int, optional): Основание системы счисления. По умолчанию 10.

        Returns:
            list[int]: Новый отсортированный список.
    """
    n = len(a)
    if n <= 1:
        return a
    positive = radix_sort_help([x for x in a if x >= 0],base)
    negative = radix_sort_help([-x for x in a if x < 0],base)
    result = [-x for x in negative[::-1]] + positive
    return result

def radix_sort_help(a: list[int], base:int) -> list[int]:
    """
        Вспомогательная функция для Radix Sort (LSD - начинаем с младшего разряда).
        Работает только с неотрицательными числами.

        Args:
            a (list[int]): Список неотрицательных чисел.
            base (int): Основание системы счисления.

        Returns:
            list[int]: Отсортированный список.
    """
    n = len(a)
    res = []
    if n <= 1:
        return a
    max_digits = len(str(max(a)))
    for i in range(max_digits):
        bins: list[list[int]] = [[] for _ in range(base)]
        for x in a:
            digit = (x // base ** i) % base
            bins[digit].append(x)
        res = [x for temp in bins for x in temp]
        a = res
    return res
def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    """
        Блочная (вёдерная) сортировка (Bucket Sort).
        Распределяет элементы по блокам, нормализуя значения к диапазону [0, 1],
        затем сортирует каждый блок отдельно (с помощью quick_sort).

        Args:
            a (list[float]): Список чисел (обычно float).
            buckets (int, optional): Количество блоков. Если None, равно длине списка.

        Returns:
            list[float]: Новый отсортированный список.
    """
    if not a:
        return []

    if buckets is None:
        buckets = len(a)

    mn, mx = min(a), max(a)

    normalized = a
    den = mx - mn
    if mn < 0 or mx > 1 or den != 0:
        if den == 0:
            return a.copy()
        normalized = [(x - mn) / den for x in a]

    B: list[list[float]] = [[] for _ in range(buckets)]
    for x in normalized:
        idx = min(int(x * buckets), buckets - 1)
        B[idx].append(x)

    for i in range(buckets):
        B[i] = quick_sort(B[i])
    sorted_norm = [x for bucket in B for x in bucket]
    if normalized is not a:
        return [x * den + mn for x in sorted_norm]

    return sorted_norm

def heapify(a: list[T], n: int, i: int,
            key: Callable[[T], Any] | None = None,
            cmp: Callable[[Any, Any], int] | None = None) -> None:
    """
        Преобразует поддерево с корнем в индексе i в двоичную кучу.
        Используется в пирамидальной сортировке.

        Args:
            a (list[T]): Список элементов.
            n (int): Размер кучи (может быть меньше длины списка).
            i (int): Индекс корня поддерева.
            key (Callable, optional): Функция ключа.
            cmp (Callable, optional): Функция сравнения.
        """
    if key is None:
        def identity(x):
            return x

        key = identity

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    def cmp_val(x, y):
        return cmp(x, y) if cmp else (x > y) - (x < y)

    if left < n and cmp_val(key(a[left]), key(a[largest])) > 0:
        largest = left
    if right < n and cmp_val(key(a[right]), key(a[largest])) > 0:
        largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest, key, cmp)

def heap_sort(a: list[T], key: Callable[[T], Any] | None = None,
              cmp: Callable[[Any, Any], int] | None = None) -> list[T]:
    """
        Пирамидальная сортировка (Heap Sort).
        Строит max-heap из списка, затем поочередно извлекает максимальный элемент
        (корень кучи) и помещает его в конец массива.

        Args:
            a (list[T]): Список для сортировки.
            key (Callable, optional): Функция ключа.
            cmp (Callable, optional): Функция сравнения.

        Returns:
            list[T]: Отсортированный список.
    """
    if key is None:
        def identity(x):
            return x

        key = identity

    n = len(a)
    if n <= 1:
        return a
    for i in range(n//2, -1, -1):
        heapify(a, n, i, key=key, cmp=cmp)
    for i in range(n-1,0,-1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0, key=key, cmp=cmp)
    return a
