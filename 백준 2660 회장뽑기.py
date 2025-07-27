# 백준 2660 회장뽑기

# 점수: 어느 회원 기준으로 다른 회원들 중 가장 거리가 먼 회원까지의 거리

def bfs(m):
    visited = [0 for _ in range(n+1)]
    visited[m] = 1
    queue = [[m,0]]
    
    score = 0
    
    while queue:
        x,s = queue.pop(0)
        score = max(score, s)
        
        for y in range(1, n+1):
            if adj[x][y] == 0 or visited[y]: continue
            visited[y] = 1
            queue.append([y, s+1])

    return score

n = int(input())
adj = [[0 for _ in range(n+1)] for _ in range(n+1)]
while 1:
    f1, f2 = map(int, input().split())
    if f1 == -1:
        break
    adj[f1][f2] = 1
    adj[f2][f1] = 1

scores = []
for m in range(1,n+1):
    scores.append(bfs(m))
    
print(min(scores), scores.count(min(scores)))
for i in range(n):
    if scores[i]==min(scores):
        print(i+1, end = ' ')
        