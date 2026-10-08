f = open("input.txt")

n,k = map(int , f.readline().split())
def sochit_cnt(n , k):
    if k < 0 or k > n:
        return 0
    if k == n or k == 0:
        return 1

    k = min(k , n - k)

    up = 1
    down = 1
    for i in range(1, k + 1):
        up *= (n - i + 1)
        down *= i
    return up // down

def sochit(start, curr_comb):
    if len(curr_comb) == k:
        print(' '.join(map(str, curr_comb)))
        return 

    for num in range(start, n - (k - len(curr_comb)) + 2):
        curr_comb.append(num)
        sochit(num + 1, curr_comb)
        curr_comb.pop()

print(sochit_cnt(n,k))
sochit(1, [])