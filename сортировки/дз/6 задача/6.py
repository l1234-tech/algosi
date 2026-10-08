f = open("input.txt")

n, m = map(int , f.readline().split())

segs  = []

for line in f:
    b , e = map(int, line.split())
    segs.append([b, e])

segs.sort()


covered = 0

curr_L , curr_R = segs[0]

for b , e in segs[1:]:
    if b > curr_R + 1:
        covered += (curr_R - curr_L + 1)
        curr_L, curr_R = b ,e 
    else:
        if e > curr_R:
            curr_R = e

covered += (curr_R - curr_L + 1)

print(n - covered)