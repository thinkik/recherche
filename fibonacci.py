"""Compute and print the first ten Fibonacci numbers."""


def fibonacci(n: int) -> list[int]:
    """Return the first n Fibonacci numbers as a list."""
    if n <= 0:
        return []

    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])

    return sequence[:n]


if __name__ == "__main__":
    numbers = fibonacci(10)
    print(" ".join(str(num) for num in numbers))
