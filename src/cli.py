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
@app.command()
def fib(n: int):
    fib_rec = fact_fib.fib_recursive(n)
    fib_iter = fact_fib.fib_iterative(n)
    typer.echo(f"Fibonacci recursive {n}: {fib_rec}\n"
               f"Fibonacci iterative {n}: {fib_iter}")
@app.command()
def fact(n: int):
    fact_rec = fact_fib.factorial_recursive(n)
    fact_iter = fact_fib.factorial_iterative(n)
    typer.echo(f"Factorial recursive {n}: {fact_rec}\n"
               f"Factorial iterative {n}: {fact_iter}")


@app.command()
def sort(
    algo: str = typer.Argument(..., help="Algorithm: bubble|quick|merge|heap|count|radix|bucket"),
    array: str = typer.Argument(..., help="Array, e.g. [5,3,1,2]"),
    key_name: str | None = typer.Option(None, "--key", help="Key function: abs | neg | str | len | first | last | parity | square | revstr"),
    cmp_name: str | None = typer.Option(None, "--cmp", help="Comparator: asc | desc | mod | revmod | str | len | first | last | even_first | odd_first"),

):
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
    res = ALGOS[algo](arr, key=key_func, cmp=cmp_func)
    typer.echo(res)


@app.command()
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
    sorted_arr = ALGOS[algo](arr.copy(),key=key_func, cmp=cmp_func)
    typer.echo(f"Sorted array: {sorted_arr}")


gen_app = typer.Typer(help="Array generators")
app.add_typer(gen_app, name="gen")
@gen_app.command("rand")
def gen_random(n: int, lo: int, hi: int):
    typer.echo(rand_int_array(n, lo, hi))


@gen_app.command("nearly")
def gen_nearly(n: int, swaps: int):
    typer.echo(nearly_sorted(n, swaps))


@gen_app.command("dups")
def gen_dups(n: int, k: int = 5):
    typer.echo(many_duplicates(n, k))


@gen_app.command("rev")
def gen_reverse(n: int):
    typer.echo(reverse_sorted(n))


@gen_app.command("float")
def gen_float(n: int, lo: float = 0.0, hi: float = 1.0):
    typer.echo(rand_float_array(n, lo, hi))


@app.command()
def bench():
    arrays = {
        "small_random": rand_int_array(200, 0, 100),
        "reverse": reverse_sorted(500),
        "nearly": nearly_sorted(500, 10),
        "dups": many_duplicates(500, k_unique=5),
    }

    results = benchmark_sorts(arrays, ALGOS)

    typer.echo(json.dumps(results, indent=4))



@app.command()
def queue(impl: str):
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

@app.command()
def stack(impl: str):
    """Интерактивная сессия со стеком. Пример: stack list"""
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




if __name__ == "__main__":
    app()
