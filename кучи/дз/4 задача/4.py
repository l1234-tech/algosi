import heapq

f = open('input.txt')

n = int(f.readline())

heap = []
heapq.heapify(heap)
total = 0

list_files = [int(x) for x in f.readline().split()]

for i in range(n):
    heapq.heappush(heap, list_files[i])

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    total += (a + b)

    heapq.heappush(heap, (a + b))
print(total)