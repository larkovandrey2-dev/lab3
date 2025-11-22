def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)
def fib_recursive(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def fib_iterative(n):
    if n <= 1:
        return n
    else:
        a, b = 1, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
if __name__ == "__main__":
    user_input = int(input("Enter a number: "))
    print(f"Factorial recursive of {user_input} = {factorial_recursive(user_input)}")
    print(f"Factorial iterative of {user_input} = {factorial_iterative(user_input)}")
    print(f"Fibonacci recursive of {user_input} = {fib_recursive(user_input)}")
    print(f"Fibonacci iterative of {user_input} = {fib_iterative(user_input)}")
