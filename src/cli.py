import typer # type: ignore
import json
import random


from src.addons.tests_generator import (
    rand_int_array, nearly_sorted, many_duplicates,
    reverse_sorted, rand_float_array
)
import src.fact_fib as fact_fib
from src.addons.benchmark import benchmark_sorts
from src.queues.queue_actions import QUEUES, queue_action
from src.stacks.stacks_actions import STACKS, stack_action
from src.config import ALGOS, GENERATORS, KEYS, CMPS

app = typer.Typer(help="CLI for sorting algorithms, benchmarks and data structures.")
@app.command(help="Вычисляет число Фибоначчи (рекурсивно и итеративно).")
def fib(n: int = typer.Argument(..., help="Номер числа Фибоначчи")):
    """
        Выводит n-ое число Фибоначчи, вычисленное двумя способами:
        рекурсивным и итеративным алгоритмами.
    """
    try:
        fib_rec = fact_fib.fib_recursive(n)
        fib_iter = fact_fib.fib_iterative(n)
        typer.echo(f"Fibonacci recursive {n}: {fib_rec}\n"
                   f"Fibonacci iterative {n}: {fib_iter}")
    except Exception as e:
        typer.echo(e)
        typer.Exit(1)
@app.command(help="Вычисляет факториал числа (рекурсивно и итеративно).")
def fact(n: int = typer.Argument(..., help="Число для вычисления факториала")):
    """
        Выводит факториал числа n, вычисленный двумя способами:
        рекурсивным и итеративным алгоритмами.
    """
    try:
        fact_rec = fact_fib.factorial_recursive(n)
        fact_iter = fact_fib.factorial_iterative(n)
        typer.echo(f"Factorial recursive {n}: {fact_rec}\n"
                   f"Factorial iterative {n}: {fact_iter}")
    except Exception as e:
        typer.echo(e)
        typer.Exit(1)


@app.command(help="Сортирует массив, заданный вручную в формате JSON.")
def sort(
    algo: str = typer.Argument(..., help="Algorithm: bubble|quick|merge|heap|count|radix|bucket"),
    array: str = typer.Argument(..., help="Array, e.g. [5,3,1,2]"),
    key_name: str | None = typer.Option(None, "--key", help="Key function: abs | neg | str | len | first | last | parity | square | revstr"),
    cmp_name: str | None = typer.Option(None, "--cmp", help="Comparator: asc | desc | mod | revmod | str | len | first | last | even_first | odd_first"),

):
    """
        Принимает строку с массивом в формате JSON и сортирует его выбранным алгоритмом.
        Позволяет применять функции ключей (--key) и кастомные компараторы (--cmp).
    """
    arr = json.loads(array)

    if algo not in ALGOS:
        typer.echo(f"Unknown algorithm '{algo}'")
        raise typer.Exit()


    key_func = None
    cmp_func = None

    if key_name:
        if key_name not in KEYS:
            typer.echo(f"Unknown key: {key_name}")
            raise typer.Exit(1)
        key_func = KEYS[key_name]

    if cmp_name:
        if cmp_name not in CMPS:
            typer.echo(f"Unknown comparator: {cmp_name}")
            raise typer.Exit(1)
        cmp_func = CMPS[cmp_name]

    if (key_name or cmp_name) and (algo in ["count", "radix", "bucket"]):
        typer.echo(f"Sort algorithm '{algo}' does not support keys/comparators")
        raise typer.Exit(1)
    if algo in ["count", "radix", "bucket"]:
        res = ALGOS[algo](arr.copy())
    else:
        res = ALGOS[algo](arr.copy(),key=key_func, cmp=cmp_func)
    typer.echo(res)


@app.command(help="Генерирует массив и сортирует его.")
def sort_generated(
    algo: str = typer.Argument(..., help="Algorithm: bubble|quick|merge|heap|count|radix"),
    generator: str = typer.Option("random", help="Generator type: random|nearly|reverse|dups|float"),
    size: int = typer.Option(10, help="Array size"),
    lo: float = typer.Option(0.0, help="Lower bound"),
    hi: float = typer.Option(100.0, help="Upper bound"),
    swaps: int = typer.Option(5, help="Number of swaps for nearly_sorted"),
    k_unique: int = typer.Option(5, help="Number of unique elements for many_duplicates"),
    distinct: bool = typer.Option(False, help="For rand_int_array: distinct elements"),
    seed: int | None = typer.Option(None, help="Seed for reproducible generation"),
    key_name: str | None = typer.Option(None, "--key", help="Key function: abs | neg | str | len | first | last | parity | square | revstr"),
    cmp_name: str | None = typer.Option(None, "--cmp", help="Comparator: asc | desc | mod | revmod | str | len | first | last | even_first | odd_first"),
):
    """
        Создает массив заданного типа и размера, выводит его, а затем сортирует.
    """
    if generator not in GENERATORS:
        typer.echo(f"Unknown generator: {generator}")
        raise typer.Exit()

    actual_seed = seed if seed is not None else random.randint(0, 1_000_000)
    if generator == "random":
        arr = rand_int_array(size, int(lo), int(hi), distinct=distinct, seed=actual_seed)
    elif generator == "nearly":
        arr = nearly_sorted(size, swaps, seed=actual_seed)
    elif generator == "reverse":
        arr = reverse_sorted(size)
    elif generator == "dups":
        arr = many_duplicates(size, k_unique=k_unique, seed=actual_seed)
    elif generator == "float":
        arr = rand_float_array(size, lo, hi, seed=actual_seed)

    typer.echo(f"Generated array ({generator}, seed={actual_seed}): {arr}")

    if algo not in ALGOS:
        typer.echo(f"Unknown algorithm: {algo}")
        raise typer.Exit()
    key_func = None
    cmp_func = None

    if key_name:
        if key_name not in KEYS:
            typer.echo(f"Unknown key: {key_name}")
            raise typer.Exit(1)
        key_func = KEYS[key_name]

    if cmp_name:
        if cmp_name not in CMPS:
            typer.echo(f"Unknown comparator: {cmp_name}")
            raise typer.Exit(1)
        cmp_func = CMPS[cmp_name]

    if (key_name or cmp_name) and (algo in ["count", "radix", "bucket"]):
        typer.echo(f"Sort algorithm '{algo}' does not support keys/comparators")
        raise typer.Exit(1)
    if algo in ["count", "radix", "bucket"]:
        sorted_arr = ALGOS[algo](arr.copy())
    else:
        sorted_arr = ALGOS[algo](arr.copy(),key=key_func, cmp=cmp_func)
    typer.echo(f"Sorted array: {sorted_arr}")


gen_app = typer.Typer(help="Утилиты для генерации массивов.")
app.add_typer(gen_app, name="gen")
@gen_app.command("rand", help="Случайные числа.")
def gen_random(n: int, lo: int, hi: int):
    """Генерирует массив случайных целых чисел."""
    typer.echo(rand_int_array(n, lo, hi))


@gen_app.command("nearly", help="Почти отсортированный массив.")
def gen_nearly(
    n: int = typer.Argument(..., help="Размер"),
    swaps: int = typer.Argument(..., help="Количество перестановок")
):
    """Генерирует отсортированный массив с несколькими случайными перестановками."""
    typer.echo(nearly_sorted(n, swaps))

@gen_app.command("dups", help="Массив с дубликатами.")
def gen_dups(
    n: int = typer.Argument(..., help="Размер"),
    k: int = typer.Option(5, help="Количество уникальных чисел")
):
    """Генерирует массив, составленный из малого количества уникальных чисел."""
    typer.echo(many_duplicates(n, k))

@gen_app.command("rev", help="Обратно отсортированный массив.")
def gen_reverse(n: int = typer.Argument(..., help="Размер")):
    """Генерирует массив от N до 1."""
    typer.echo(reverse_sorted(n))

@gen_app.command("float", help="Массив чисел с плавающей точкой.")
def gen_float(
    n: int = typer.Argument(..., help="Размер"),
    lo: float = typer.Option(0.0, help="Мин"),
    hi: float = typer.Option(1.0, help="Макс")
):
    """Генерирует массив float чисел в заданном диапазоне."""
    typer.echo(rand_float_array(n, lo, hi))

@app.command(help="Запускает стандартный набор бенчмарков.")
def bench():
    """
        Запускает предопределенный набор тестов производительности
        на фиксированных массивах (random, reverse, nearly, dups).
    """
    arrays = {
        "small_random": rand_int_array(1000, 0, 100),
        "big_random": rand_int_array(5000, 0, 100),
        "reverse": reverse_sorted(1000),
        "nearly": nearly_sorted(1000, 10),
        "dups": many_duplicates(1000, k_unique=5),
        "dups_big": many_duplicates(8000, k_unique=5),
    }

    results = benchmark_sorts(arrays, ALGOS)

    typer.echo(json.dumps(results, indent=4))


@app.command(help="Интерактивная сессия с очередью.")
def queue(impl: str):
    """
        Запускает интерактивный режим работы с выбранной реализацией очереди.
    """
    if impl not in QUEUES:
        typer.echo(f"Неизвестная реализация: {impl}")
        typer.echo(f"Доступные: {', '.join(QUEUES.keys())}")
        raise typer.Exit(1)
    QueueClass = QUEUES[impl]
    q = QueueClass()

    typer.echo(f"\n Очередь создана: {impl}")
    typer.echo("Команды: enqueue X | dequeue | front | size | empty | quit")

    while True:
        cmd = typer.prompt("queue> ")

        if cmd == "quit":
            break

        parts = cmd.split()
        action = parts[0]
        value = None
        if len(parts) > 1:
            try:
                value = int(parts[1])
            except ValueError:
                typer.echo("Ошибка: нужно вводить число")
                continue

        try:
            res = queue_action(q, action, value)
            typer.echo(f"-> {res}")
        except Exception as e:
            typer.echo(f"Ошибка: {e}")

@app.command(help="Интерактивная сессия со стеком.")
def stack(impl: str):
    """Интерактивная сессия со стеком."""
    if impl not in STACKS:
        typer.echo(f"Неизвестная реализация: {impl}")
        typer.echo(f"Доступные: {', '.join(STACKS.keys())}")
        raise typer.Exit(1)

    StackClass = STACKS[impl]
    s = StackClass()

    typer.echo(f"\n Стек создан: {impl}")
    typer.echo("Команды: push X | pop | peek | size | empty | quit")

    while True:
        cmd = typer.prompt("stack> ")

        if cmd == "quit":
            break

        parts = cmd.split()
        action = parts[0]
        value = None

        if len(parts) > 1:
            try:
                value = int(parts[1])
            except ValueError:
                typer.echo("Ошибка: нужно вводить число")
                continue

        try:
            res = stack_action(s, action, value)
            typer.echo(f"-> {res}")
        except Exception as e:
            typer.echo(f"Ошибка: {e}")


@app.command(help="Запускает кастомный бенчмарк на серии размеров.")
def bench_custom(
        algos: list[str] = typer.Option(None, "--algo", "-a", help="Algorithms to test. If empty, runs all."),
        generator: list[str] = typer.Option("random", help="Generator type: random|nearly|reverse|dups|float"),
        sizes: list[int] = typer.Option([100, 1000, 5000], "--size", "-s", help="Sizes of arrays to generate"),
        lo: float = typer.Option(0.0, help="Lower bound"),
        hi: float = typer.Option(100.0, help="Upper bound"),
        swaps: int = typer.Option(10, help="Number of swaps for nearly_sorted"),
        k_unique: int = typer.Option(5, help="Number of unique elements for many_duplicates"),
        distinct: bool = typer.Option(False, help="For rand_int_array: distinct elements"),
        seed: int | None = typer.Option(None, help="Seed for reproducible generation"),
):
    """
        Функция позволяет выбрать конкретные алгоритмы и проверить их на массивах разных размеров.
    """
    selected_algos = {}

    target_algos_names = algos if algos else ALGOS.keys()

    for name in target_algos_names:
        if name in ALGOS:
            selected_algos[name] = ALGOS[name]
        else:
            typer.echo(f"Предупреждение: Алгоритм '{name}' не найден, пропускаем.")

    if not selected_algos:
        typer.echo("Ошибка: Не выбрано ни одного валидного алгоритма.")
        raise typer.Exit(1)
    arrays_to_test = {}
    actual_seed = seed if seed is not None else random.randint(0, 1_000_000)
    typer.echo(f"Running benchmark with seed: {actual_seed}")
    for gen in generator:
        for size in sizes:
            label = f"{gen}_size_{size}"
            if gen == "random":
                arr = rand_int_array(size, int(lo), int(hi), distinct=distinct, seed=actual_seed)
            elif gen == "nearly":
                arr = nearly_sorted(size, swaps, seed=actual_seed)
            elif gen == "reverse":
                arr = reverse_sorted(size)
            elif gen == "dups":
                arr = many_duplicates(size, k_unique=k_unique, seed=actual_seed)
            elif gen == "float":
                arr = rand_float_array(size, lo, hi, seed=actual_seed)
            else:
                typer.echo(f"Неизвестный генератор: {gen}")
                raise typer.Exit(1)

            arrays_to_test[label] = arr
    results = benchmark_sorts(arrays_to_test, selected_algos)
    typer.echo(json.dumps(results, indent=4))

if __name__ == "__main__":
    app()
