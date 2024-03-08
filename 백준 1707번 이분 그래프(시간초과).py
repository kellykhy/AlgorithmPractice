# 백준 1707번 이분 그래프(시간초과)

import sys
input = sys.stdin.readline

def backtrack(v):
    cycle_v_num = 1 + list(reversed(history)).index(v) # if cycle = (1,2,0) -> backtrack(0), history = [7,6,5,3,0,1,2]
    if (cycle_v_num % 2 == 1):
        return 1 # this means it is NOT 이분그래프
    else:
        return 0

# 케이스 하나라고 가정하기
def dfs(v, prt):
    stack = []
    stack.append((v, prt))
    flag = 0
    while(stack):
        cur_v, cur_prt = stack.pop()
        visited[cur_v] = 1
        history.append(cur_v)
        for new_v in graph[cur_v]:
            if (visited[new_v] == 1):
                if (new_v != cur_prt):
                    if (backtrack(new_v) == 1):
                        flag = 1
                continue
            stack.append((new_v, cur_v))
            if (flag == 1):
                break
    if (flag == 0):
        return 1
    else:
        return 0
        

#input
K = int(input())
history = []

for _ in range(K):
    V, E = map(int, input().split())
    history = []
    visited = [0] * (V+1)
    graph = [[] for _ in range(V+1)] # 첫번째 원소 = 정점개수(V), 간선개수(E) 저장
    flag = 0
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, V+1):
        if (visited[i] == 0):
            result = dfs(i, -1)
            if (not result):
                break
    print("YES" if result else "NO")
    

# 나의 시도: 사이클이 존재하면서, 사이클을 이루는 정점의 개수가 홀수이면 -> [이분그래프 위배]로 판단했음
# -> 시간 초과 (결과는 맞는듯.)

# 바른 풀이: 인접 노드가 동일 그룹(1, -1로 구분)에 속하면 [이분그래프 위배]로 판단