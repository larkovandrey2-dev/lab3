import random

def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None):
    if seed is not None:
        random.seed(seed)
    if distinct:
        return random.sample(range(lo, hi), n)
    else:
        return [random.randint(lo, hi) for _ in range(n)]

def nearly_sorted(n: int, swaps: int, *, seed=None):
    if seed is not None:
        random.seed(seed)
    arr = list(range(n))
    for _ in range(swaps):
        i,j = random.randint(0,n-1), random.randint(0,n-1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr
def many_duplicates(n: int, k_unique=5, *, seed=None):
    if seed is not None:
        random.seed(seed)
    choices = [random.randint(0,10000) for _ in range(k_unique)]
    return [random.choice(choices) for _ in range(n)]
def reverse_sorted(n: int):
    return list(range(n, 0, -1))
def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None):
    if seed is not None:
        random.seed(seed)
    return [random.uniform(lo, hi) for _ in range(n)]
