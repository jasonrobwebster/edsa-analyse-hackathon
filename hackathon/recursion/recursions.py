__all__ = [
    'sum_array',
    'factorial',
    'fibonacci',
    'reverse'
]

def sum_array():
    # Not properly defined
    return

def factorial(n):
    if n < 0:
        raise TypeError('Given value is less than 0!')
    if n == 0:
        return 1
    return n * factorial(n-1)

def fibonacci(x):
    if x <0:
        raise TypeError('Given value is less than 0!')
    if x == 0 or x==1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

def reverse():
    # Not properly defined
    return