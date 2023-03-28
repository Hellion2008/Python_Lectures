"""
Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
"""
def fib (n):
    res = 1
    if n == 1 or n == 0:
        return res
    return fib(n - 1) + fib(n - 2)

print(fib(7))