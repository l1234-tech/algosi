f = open("input.txt")
stroka = sorted(list(map(int, f.readline().split())), reverse=True)

ost_0 = sorted([x for x in stroka if x % 3 == 0], reverse=True)
ost_1 = sorted([x for x in stroka if x % 3 == 1], reverse=True)
ost_2 = sorted([x for x in stroka if x % 3 == 2], reverse=True)

result = []

if len(ost_0) >= 2:
    result.append(ost_0[0] + ost_0[1])

if len(ost_1) >= 1 and len(ost_2) >= 1:
    result.append(ost_2[0] + ost_1[0])

if result:
    print(max(result))
else:
    print(-1)