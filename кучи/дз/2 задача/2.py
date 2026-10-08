import heapq

f = open('input.txt')

k = int(f.readline())

arrs = []

for _ in range(k):
    s = list(map(int, f.readline().split()))
    n = s[0]
    arrs.append(s[1:])

heap = []

for i in range(k):
    if arrs[i]:
        heap.append((arrs[i][0] , i, 0))

heapq.heapify(heap)

res = []

while heap:
    val , idx , idx_arr = heapq.heappop(heap)
    res.append(val)
    if idx_arr + 1 < len(arrs[idx]):
        heapq.heappush(heap, (arrs[idx][idx_arr + 1], idx, idx_arr + 1))




print(' '.join(map(str, res)))