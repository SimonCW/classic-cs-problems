from typing import Generator
import pytest
from functools import lru_cache

""" 0 1 1 2 3 5 8 13 21 """


@lru_cache(maxsize=None)
def fib_rec(n: int) -> int:
    if n < 2:
        return n
    return fib_rec(n - 2) + fib_rec(n - 1)


def fib_it(n: int) -> int:
    if n == 0:
        return n
    last: int = 0
    next: int = 1

    for _ in range(1, n):
        old_next: int = next
        next = last + next
        last = old_next
    return next


def fib_gen(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last + next
        yield next


@pytest.mark.parametrize("fib_func", [fib_it, fib_rec])
def test_fib_fourth_equal_two(fib_func):
    assert fib_func(3) == 2


@pytest.mark.parametrize("fib_func", [fib_it, fib_rec])
def test_fib_eight_equal_thirteen(fib_func):
    assert fib_func(7) == 13


if __name__ == "__main__":
    for i in fib_gen(10):
        print(i)
