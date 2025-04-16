# 백준 2164번 카드2

from collections import deque

N = int(input())
cards = deque()
for n in range(1, N+1):
    cards.append(n)
    
for i in range(N-1):
    cards.popleft()
    cards.append(cards.popleft())
print(cards[0])