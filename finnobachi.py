# %%
#finding n value of finnobachi
def fib1 (n : int) -> int:
    if n < 2:
        return n 
    return  fib1(n - 2) + fib1(n - 1)


# memo with dict
from typing import Dict
memo: Dict[int, int] = {0 : 0, 1 : 1}
def fib_memo(n : int):
    if n not in memo:
       memo[n] = fib_memo( n - 2 ) + fib_memo( n - 1 )
    return memo[n]

# the simle way
def fib_loop(n: int) -> int:
    if n == 0: return 0

    prev: int = 0 
    curr: int = 1

    for _ in range(1, n):
        prev, curr = curr, prev + curr
    return curr


def fib_gen(n: int):
    yield 0
    if n == 1: yield 1

    prev: int = 0 
    curr: int = 1

    for _ in range(1, n):
        prev, curr = curr, prev + curr
        yield curr

# %%
print(fib_memo(5))
print(fib1(5))
print(fib_loop(5))

print (fib1(20))
print(fib_memo(20))
print(fib_loop(20))


# %%
for i in fib_gen(20):
    print(i)
