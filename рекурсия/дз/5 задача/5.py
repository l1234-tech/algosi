import sys

def hanoi(n , frm, to, aux, out):
    if n == 0:
        return
    hanoi(n - 1, frm, aux, to, out)
    out.append(f"{n} {frm} {to}")
    hanoi(n - 1, aux, to, frm, out)

def solution():
    f = open("input.txt")
    n = int(f.readline())
    out = []
    hanoi(n, 1, 3, 2, out)
    sys.stdout.write(str(len(out)) + "\n" + "\n".join(out))

solution()