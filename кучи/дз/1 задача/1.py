import heapq

f = open('input.txt')

n, m = map(int , f.readline().split())

buff = [int(x) for x in f.readline().split()]

def solve(arr, m):
    heapq.heapify(arr)
    cnt = 1
    while cnt < m:
        heapq.heappop(arr)
        cnt += 1

    return (heapq.heappop(arr))

print(solve(buff , m))