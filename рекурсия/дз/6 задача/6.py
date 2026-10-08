import sys
f = open('input.txt')

n = int(f.readline())

c = [0] * n
res = []

cols = set()   
d1 = set()      
d2 = set()      

def place(row):
    if row == n:
        res.append(c[:])
        return
    for col in range(1, n + 1):
        if col in cols:
            continue
        if (row + col) in d1:
            continue
        if (row - col) in d2:
            continue

        c[row] = col
        cols.add(col)
        d1.add(row + col)
        d2.add(row - col)

        place(row + 1)

        cols.remove(col)
        d1.remove(row + col)
        d2.remove(row - col)

place(0)

if not res:
    print(0)
    sys.exit()

out = [str(len(res))]
for r in res:
    out.append(' '.join(map(str, r)))
sys.stdout.write('\n'.join(out))