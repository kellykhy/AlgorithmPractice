# 백준 1197번 최소 스패닝 트리
import sys
input = sys.stdin.readline

def find(v1):
    if p[v1] < 0 : return v1
    else: 
        p[v1] = find(p[v1])
        return p[v1]

def is_diff_group(v1, v2):
    v1, v2 = find(v1), find(v2)
    if (v1 == v2): 
        return 0 # 부모가 다르지 않음(같음)
    else:
        if p[v1] == p[v2]: p[v1] -= 1 # v1의 rank 1 증가 (바로 아래 코드로 이어져서 실행)
        if p[v1] < p[v2]: p[v2] = v1 # v2의 부모가 v1이 됨
        else: p[v1] = v2 # v1의 부모가 v2가 됨
        return 1
    

v, e = map(int, input().split())
edges = []
for i in range(e):
    edges.append(list(map(int, input().split())))
    
edges.sort(key=lambda x:x[2])
p = [-1 for _ in range(v+1)] # union-by-rank : p[u]가 양수일 땐 부모의 번호이고, 음수일 땐 -p[u]가 u의 랭크임!!

cnt = 0
result = 0
for i in range(e):
    v1, v2, c = edges[i]
    if not is_diff_group(v1, v2): continue
    cnt += 1
    result += c
    if cnt == v-1: break

print(result)