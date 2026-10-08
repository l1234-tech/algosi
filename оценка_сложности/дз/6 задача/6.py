f = open("input.txt")
stroka = list(map(int, f.readline().split()))

ost_1 = sorted([x for x in stroka if x % 3 == 1])
ost_2 = sorted([x for x in stroka if x % 3 == 2])

result = sum(stroka)

flag = result % 3

if flag == 0:
    result = result

if flag == 1:
    candidats = []
    if len(ost_2) >= 2:
        candidats.append(sum(ost_2[:2]))
    if len(ost_1) > 0:
        candidats.append(ost_1[0])
    if candidats:
        result -= min(candidats)
    else:
        result = -1

if flag == 2:
    candidats = []
    if len(ost_1) >= 2:
        candidats.append(sum(ost_1[:2]))
    if len(ost_2) > 0:
        candidats.append(ost_2[0])
    if candidats:
        result -= min(candidats)
    else:
        result = -1

print(result)