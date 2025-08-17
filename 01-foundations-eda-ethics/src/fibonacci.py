def generate_fib(n):
    """
    Generate the first n Fibonacci numbers using a for loop.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        list: A list containing the first n Fibonacci numbers.
    """
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage:
print(generate_fib(10)) 