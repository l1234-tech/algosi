f = open("input.txt")
from functools import cmp_to_key
n = int(f.readline())
a = [int(s) for s in f.readline().split()]

mid = n // 2

def compare(a,b):
    x, y = str(a), str(b)
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    return 0

left = sorted(a[:mid + 1], key=cmp_to_key(compare))
right = sorted(a[mid + 1:], key=cmp_to_key(compare))

def merge(left, right):
    lf = 0
    rg = 0
    res = []
    while lf < len(left) and rg < len(right):
        if compare(left[lf], right[rg]) == -1:
            res.append(left[lf])
            lf += 1
        else:
            res.append(right[rg])
            rg += 1
    res.extend(left[lf:])
    res.extend(right[rg:])
    return res

res = "".join(map(str, merge(left, right)))
if res[0] == "0":
    print(0)
else:
    print(res)