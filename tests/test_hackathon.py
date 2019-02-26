import hackathon

from hackathon.sorting import bubble_sort, merge_sort, quick_sort
from hackathon.recursion import sum_array, factorial, fibonacci, reverse

try:
    # these unit tests make use of pytest
    # run `pip install pytest` to install
    import pytest
except ImportError:
    pass


def test_bubble_sort():
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([3, 1, 2, 5, 4]) == [1, 2, 3, 4, 5]

def test_merge_sort():
    #assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([3, 1, 2, 5, 4]) == [1, 2, 3, 4, 5]

def test_quick_sort():
    assert quick_sort([]) == []
    assert quick_sort([1]) == [1]
    assert quick_sort([3, 1, 2, 5, 4]) == [1, 2, 3, 4, 5]


def test_sum_array():
    # TODO: Define sum_array
    pass

def test_fibonacci():
    with pytest.raises(TypeError):
        fibonacci(-1)
    assert fibonacci(0) == 1
    assert fibonacci(1) == 1
    assert fibonacci(2) == 2
    assert fibonacci(3) == 3
    assert fibonacci(4) == 5

def test_factorial():
    with pytest.raises(TypeError):
        factorial(-1)
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24

def test_reverse():
    # TODO: Define reverse
    pass
