"""
Simple calculator module with basic mathematical operations.
"""


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract second number from first number."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide first number by second number."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Raise first number to the power of second number."""
    return a ** b