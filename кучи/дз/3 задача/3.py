import heapq
import sys

f = open('input.txt')

n = int(f.readline())

low = []
heapq.heapify(low)
high = []
heapq.heapify(high)
res = []

for _ in range(n):
    buff = list(map(str , f.readline().split()))
    if buff[0] == "ADD":
        heapq.heappush(low, -int(buff[1]))

        heapq.heappush(high , -heapq.heappop(low))

        if len(low) < len(high):
            heapq.heappush(low, -heapq.heappop(high))

    else:

        res.append(str(-low[0]))

sys.stdout.write('\n'.join(res))