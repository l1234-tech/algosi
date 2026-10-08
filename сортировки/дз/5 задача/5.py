f = open("input.txt")

n = int(f.readline())

all_par = []

for line in f:
    line_prop = [x for x in line.split()]
    all_par.append([-int(line_prop[1]) , int(line_prop[2]), str(line_prop[0])])
res = sorted(all_par)

for x in res:
    print(x[2])