# 24416


def fib1(n):
    if n == 1 or n == 2:
        return 1;
    else:
        return (fib1(n - 1) + fib1(n - 2))

N = int(input())

print(fib1(N), (N-2))