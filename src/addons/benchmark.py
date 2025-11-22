import time
from copy import deepcopy
from typing import Callable


def timeit_once(func, *args, **kwargs) -> float:

    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start
def benchmark_sorts(arrays: dict[str, list], algos: dict[str, Callable]) -> dict[str, dict[str, float]]:
    results: dict = {}
    for arr_name, arr in arrays.items():
        results[arr_name] = {}
        for algo_name, algo in algos.items():
            arr_copy = deepcopy(arr)
            t = timeit_once(algo, arr_copy)
            results[arr_name][algo_name] = t
    return results
