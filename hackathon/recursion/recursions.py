__all__ = [
    'sum_array',
    'factorial',
    'fibonacci',
    'reverse'
]

def sum_array(array):
    if len(array) == 0:
        return 0
    return array[0] + sum_array(array[1:])

def factorial(n):
    if n < 0:
        raise TypeError('Given value is less than 0!')
    if n == 0:
        return 1
    return n * factorial(n-1)

def fibonacci(x):
    if x < 0:
        raise TypeError('Given value is less than 0!')
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

def reverse(word):
    if len(word) == 0:
        return ''
    return word[-1] + reverse(word[:-1])