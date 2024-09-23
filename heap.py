import heapq

minheap = []
maxheap = []
values = [1,5,3,2,4]

for value in values:
    heapq.heappush(minheap, value)

for i in range(5):
	print(heapq.heappop(minheap))
 
print()
 
for value in values:
    heapq.heappush(maxheap, -value)

for i in range(5):
    print(-heapq.heappop(maxheap))