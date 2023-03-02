from typing import Dict
from typing import Generator
from functools import lru_cache

def fib2(n: int) -> int:
    if n < 2:  # base case
        return n
    return fib2(n - 1) + fib2(n - 2)


memo: Dict[int, int] = {0: 0, 1: 1}
def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]

@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:  # base case
        return n
    return fib4(n - 1) + fib4(n - 2)

def fib5(n: int) -> int:
    if n == 0: return n     # special case
    last: int = 0
    next: int = 1
    for _ in range(1,n):
        last, next = next, last + next
    return next

def fib6(n: int) -> Generator[int, None, None]:
    yield 0     # special case
    if n > 0: yield 1   # special case
    last: int = 0
    next: int = 1
    for _ in range(1,n):
        last, next = next, last + next
        yield next

if __name__ == '__main__':
    print(fib3(100))
    print(fib4(100))
    print(fib5(100))
    for i in fib6(50):
        print(i)
