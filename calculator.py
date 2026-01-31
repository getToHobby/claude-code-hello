"""
A simple calculator module for performing addition, subtraction, multiplication, and division of two integers.
"""

def add(a, b):
    """
    Calculate the sum of two integers

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: Sum of two integers
    """
    return a + b


def subtract(a, b):
    """
    Calculate the difference of two integers

    Args:
        a (int): Minuend
        b (int): Subtrahend

    Returns:
        int: Difference of two integers
    """
    return a - b


def multiply(a, b):
    """
    Calculate the product of two integers

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: Product of two integers
    """
    return a * b


def divide(a, b):
    """
    Calculate the quotient of two integers

    Args:
        a (int): Dividend
        b (int): Divisor

    Returns:
        float: Quotient of two integers

    Raises:
        ZeroDivisionError: Raised when divisor is zero
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b


def integer_divide(a, b):
    """
    Calculate the floor division result of two integers

    Args:
        a (int): Dividend
        b (int): Divisor

    Returns:
        int: Floor division result of two integers

    Raises:
        ZeroDivisionError: Raised when divisor is zero
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a // b


def modulo(a, b):
    """
    Calculate the modulo (remainder) of two integers

    Args:
        a (int): Dividend
        b (int): Divisor

    Returns:
        int: Remainder after division of two integers

    Raises:
        ZeroDivisionError: Raised when divisor is zero
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a % b


if __name__ == "__main__":
    # Test cases
    print("=== Calculator Test Cases ===")

    # Addition tests
    print("\n--- Addition Tests ---")
    test_cases_add = [
        (2, 3),
        (-1, 5),
        (10, -7),
        (0, 8),
        (-3, -4)
    ]
    for a, b in test_cases_add:
        result = add(a, b)
        print(f"{a} + {b} = {result}")

    # Subtraction tests
    print("\n--- Subtraction Tests ---")
    test_cases_subtract = [
        (5, 3),
        (10, 7),
        (-1, 5),
        (0, 8),
        (-3, -4)
    ]
    for a, b in test_cases_subtract:
        result = subtract(a, b)
        print(f"{a} - {b} = {result}")

    # Multiplication tests
    print("\n--- Multiplication Tests ---")
    test_cases_multiply = [
        (2, 3),
        (-1, 5),
        (10, -7),
        (0, 8),
        (-3, -4)
    ]
    for a, b in test_cases_multiply:
        result = multiply(a, b)
        print(f"{a} * {b} = {result}")

    # Division tests
    print("\n--- Division Tests ---")
    test_cases_divide = [
        (10, 2),
        (15, 3),
        (-8, 2),
        (7, -1),
        (-12, -3)
    ]
    for a, b in test_cases_divide:
        result = divide(a, b)
        print(f"{a} / {b} = {result}")

    # Floor division tests
    print("\n--- Floor Division Tests ---")
    test_cases_int_divide = [
        (10, 3),
        (15, 4),
        (-8, 3),
        (7, -2),
        (-12, -5)
    ]
    for a, b in test_cases_int_divide:
        result = integer_divide(a, b)
        print(f"{a} // {b} = {result}")

    # Modulo tests
    print("\n--- Modulo Tests ---")
    test_cases_modulo = [
        (10, 3),
        (15, 4),
        (-8, 3),
        (7, -2),
        (-12, -5)
    ]
    for a, b in test_cases_modulo:
        result = modulo(a, b)
        print(f"{a} % {b} = {result}")

    # Exception handling tests
    print("\n--- Exception Handling Tests ---")
    try:
        result = divide(10, 0)
        print("Error: Division by zero was not properly handled")
    except ZeroDivisionError as e:
        print(f"Correctly caught exception: {e}")

    try:
        result = integer_divide(10, 0)
        print("Error: Division by zero was not properly handled")
    except ZeroDivisionError as e:
        print(f"Correctly caught exception: {e}")

    try:
        result = modulo(10, 0)
        print("Error: Division by zero was not properly handled")
    except ZeroDivisionError as e:
        print(f"Correctly caught exception: {e}")