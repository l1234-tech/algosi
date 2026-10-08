f = open("input.txt")
stroka = list(map(int, f.readline().split()))

mx_sum = sum(stroka)

if mx_sum % 2 == 0:
    mx_sum = mx_sum
else:
    ne_chet = [x for x in stroka if x % 2 == 1]
    if len(ne_chet) % 2 == 1:
        mx_sum -= min(ne_chet)
    elif not ne_chet:
        mx_sum = -1 
    else:
        mx_sum = mx_sum

print(mx_sum if mx_sum >= 0 else -1)