def factorial_recursive(n):
    """
        Вычисляет факториал числа n, используя рекурсию.

        Args:
            n (int): Неотрицательное целое число.

        Returns:
            int: Факториал числа n (n!).
    """
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)
def fib_recursive(n):
    """
        Вычисляет n-е число последовательности Фибоначчи рекурсивно.

        Args:
            n (int): Порядковый номер числа (начиная с 0).

        Returns:
            int: Число Фибоначчи.
    """
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)
def factorial_iterative(n):
    """
        Вычисляет факториал числа n, используя итеративный подход (цикл).

        Args:
            n (int): Неотрицательное целое число.

        Returns:
            int: Факториал числа n (n!).
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def fib_iterative(n):
    """
        Вычисляет n-е число последовательности Фибоначчи итеративно.

        Args:
            n (int): Порядковый номер числа.

        Returns:
            int: Число Фибоначчи.
    """
    if n <= 1:
        return n
    else:
        a, b = 1, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
