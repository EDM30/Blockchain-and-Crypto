def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def factorial(n):
    """Return the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

def main():
    print(greet("Alice"))
    print(f"3 + 5 = {add(3, 5)}")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Is 4 even? {is_even(4)}")

if __name__ == "__main__":
    main()