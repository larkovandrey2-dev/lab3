from typing import Dict, Callable, Any

from src.addons.tests_generator import (
    rand_int_array, nearly_sorted, many_duplicates,
    reverse_sorted, rand_float_array
)
from src.sorts import (
    bubble_sort, quick_sort, merge_sort,
    heap_sort, count_sort, radix_sort, bucket_sort
)


GENERATORS = {
    "random": rand_int_array,
    "nearly": nearly_sorted,
    "reverse": reverse_sorted,
    "dups": many_duplicates,
    "float": rand_float_array
}
ALGOS: Dict[str, Callable[..., list]] =  {
    "quick": quick_sort,
    "merge": merge_sort,
    "heap": heap_sort,
    "count": count_sort,
    "radix": radix_sort,
    "bucket": bucket_sort,
    "bubble": bubble_sort
}
KEYS: Dict[str, Callable[[Any], Any]] = {
    "identity": lambda x: x,
    "abs": abs,
    "neg": lambda x: -x,
    "str": lambda x: str(x),
    "len": lambda x: len(x) if hasattr(x, "__len__") else 0,
    "first": lambda x: x[0] if hasattr(x, "__getitem__") else x,
    "last": lambda x: x[-1] if hasattr(x, "__getitem__") else x,
    "parity": lambda x: x % 2,
    "square": lambda x: x * x,
    "revstr": lambda x: str(x)[::-1],
}

def _cmp(a, b): return (a > b) - (a < b)

CMPS: Dict[str, Callable[[Any, Any], int]] = {
    "asc": lambda a, b: _cmp(a, b),
    "desc": lambda a, b: _cmp(b, a),
    "mod": lambda a, b: _cmp(abs(a), abs(b)),
    "revmod": lambda a, b: _cmp(abs(b), abs(a)),
    "str": lambda a, b: _cmp(str(a), str(b)),
    "len": lambda a, b: _cmp(len(a), len(b)),
    "first": lambda a, b: _cmp(a[0], b[0]),
    "last": lambda a, b: _cmp(a[-1], b[-1]),
    "even_first": lambda a, b: (a % 2) - (b % 2),
    "odd_first": lambda a, b: (b % 2) - (a % 2),
}
