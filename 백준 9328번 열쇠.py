# 백준 9328번 열쇠

# 추가로 최적화 가능한 부분: 문서 개수 미리 알아내기 -> 문서 다 얻으면 반복문 탈출
import sys
input = sys.stdin.readline

c = int(input())
for _ in range(c):
    h, w = map(int, input().split())
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    stack = []
    graph = []
    keys = [0 for _ in range(26)]
    locked = dict()
    result = 0
    for i in range(h):
        tmp = input().rstrip()
        row = []
        for j in range(w):
            row.append(tmp[j])
            if tmp[j] != '*' and (i == 0 or i == h-1 or j == 0 or j == w-1):
                stack.append((i,j))
                visited[i][j] = 1
        graph.append(row)
    key_input = input().rstrip()
    if key_input != "0":
        for i in range(len(key_input)):
            keys[ord(key_input[i])-ord('a')] = 1
    # dfs 시작
    while stack:
        x, y = stack.pop()
        if 'A' <= graph[x][y] <= 'Z':
            if not keys[ord(graph[x][y])-ord('A')]:
                if graph[x][y] in locked:
                    locked[graph[x][y]].append((x,y))
                else:
                    locked[graph[x][y]] = [(x,y)]
                continue
        elif 'a' <= graph[x][y] <= 'z':
            keys[ord(graph[x][y])-ord('a')] = 1 # 열쇠 수집
            locked_door = chr(ord('A') + ord(graph[x][y]) - ord('a'))
            if locked_door in locked:
                for j in range(len(locked[locked_door])):
                    stack.append(locked[locked_door][j])
                    graph[locked[locked_door][j][0]][locked[locked_door][j][1]] = '.'
        elif graph[x][y] == '$': # 문서 획득
            result += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w: continue
            if visited[nx][ny]: continue
            if graph[nx][ny] == '*': continue # 벽이면 다른 길로!
            visited[nx][ny] = 1
            stack.append((nx,ny))
    print(result)