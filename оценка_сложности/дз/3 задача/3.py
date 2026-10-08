f = open("input.txt")
stroka = sorted(list(map(int, f.readline().split())), reverse=True)

mx_sum = 0
if len(stroka) == 1 or len(stroka) == 0:
    mx_sum = -1
else:
    chet = sorted([x for x in stroka if x % 2 == 0], reverse=True)
    ne_chet = sorted([x for x in stroka if x % 2 == 1], reverse=True)
    if len(chet) == 1 and len(ne_chet) == 1:
        mx_sum = -1
    elif len(chet) >= 2 and len(ne_chet) < 2:
        mx_sum = chet[0] + chet[1]
    elif len(chet) < 2 and len(ne_chet) >= 2:
        mx_sum = ne_chet[0] + ne_chet[1]
    else:
        sum_chet = chet[0] + chet[1]
        sum_ne_chet = ne_chet[0] + ne_chet[1]
        if sum_chet >= sum_ne_chet:
            mx_sum = sum_chet
        else:
            mx_sum = sum_ne_chet
if mx_sum == 0:
    mx_sum = -1
print(mx_sum)