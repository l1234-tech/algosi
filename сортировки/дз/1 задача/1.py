f = open("input.txt")

n, m = map(int , f.readline().split())

left = [int(s) for s in f.readline().split()]
right = [int(s) for s in f.readline().split()]

def merge(left, right):
    lf = 0
    rg = 0
    res = []
    while lf < len(left) and rg < len(right):
        if left[lf] < right[rg]:
            res.append(left[lf])
            lf += 1
        else:
            res.append(right[rg])
            rg += 1
    res.extend(left[lf:])
    res.extend(right[rg:])
    return res

print(" ".join(map(str, merge(left, right))))