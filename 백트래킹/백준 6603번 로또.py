# 백준 6603번 로또

cases = []
while (1):
    case = list(map(int, input().split()))
    if (len(case) == 1):
        break
    cases.append(case)

ary = []
visited = [0 for _ in range(50)]

def backtracking(k, n): # n: 테스트케이스 index (0부터 시작)
    if (k == 6):
        print(*ary)
        return
    for i in range(1, cases[n][0]+1):
        if (not visited[i]):
            if (len(ary) and ary[-1] > cases[n][i]):
                continue
            visited[i] = 1
            ary.append(cases[n][i])
            backtracking(k+1, n)
            visited[i] = 0
            ary.pop()
    
for n in range(len(cases)):
    visited = [0 for _ in range(50)]
    ary.clear()
    backtracking(0, n)
    print()