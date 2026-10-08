n, m = map(int, input().split())

def fib(n, acc_1=1, acc_2=1):
    while n >= 2:
        n, acc_1, acc_2 = n - 1, acc_2, acc_1 + acc_2
    if n == 0:
        return acc_1
    if n == 1:
        return acc_2

print(fib(n) % m)