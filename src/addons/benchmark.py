import time
from copy import deepcopy
from typing import Callable


def timeit_once(func, *args, **kwargs) -> float:
    """
        Замеряет время однократного выполнения переданной функции.
        Args:
            func (Callable): Функция, которую необходимо протестировать.
            *args: Позиционные аргументы для передачи в func.
            **kwargs: Именованные аргументы для передачи в func.

        Returns:
            float: Время выполнения функции в секундах.
    """
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start
def benchmark_sorts(arrays: dict[str, list], algos: dict[str, Callable]) -> dict[str, dict[str, float]]:
    """
        Проводит сравнительное тестирование (бенчмарк) заданных алгоритмов сортировки
        на предоставленных наборах данных.

        Args:
            arrays (dict[str, list]): Словарь наборов данных, где ключ — название набора
                (например, "random"), а значение — список элементов.
            algos (dict[str, Callable]): Словарь алгоритмов сортировки, где ключ — название
                алгоритма, а значение — вызываемый объект (функция сортировки).

        Returns:
            dict[str, dict[str, float]]: Словарь результатов.
    """
    results: dict = {}
    for arr_name, arr in arrays.items():
        results[arr_name] = {}
        for algo_name, algo in algos.items():
            arr_copy = deepcopy(arr)
            t = timeit_once(algo, arr_copy)
            results[arr_name][algo_name] = t
    return results
