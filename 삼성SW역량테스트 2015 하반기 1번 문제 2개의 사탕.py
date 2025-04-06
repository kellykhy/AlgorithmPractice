# 백준 13460번 구슬 탈출 2(삼성SW역량테스트 2015 하반기 1번 문제)

import sys
from collections import deque
input = sys.stdin.readline
OUT = ([-1, -1], -1)

N, M = map(int, input().split())

box = []
red, blue = [0,0], [0,0]
exit = [0,0]
for i in range(N):
    row = input()
    rowlist = []
    for j in range(M):
        if row[j] == 'R':
            red = [i, j]
            rowlist.append('.')
        elif row[j] == 'B':
            blue = [i, j]
            rowlist.append('.')
        elif row[j] == 'O':
            exit = i,j
            rowlist.append('O')
        else:
            rowlist.append(row[j])
    box.append(rowlist)

def move(location, dir):
    x, y = location
    steps = 0
    while 1:
        nx, ny = x + dir[0], y + dir[1]
        if not (0 <= nx < N and 0 <= ny < M) or box[nx][ny] == '#':
            return ([x,y], steps)
        elif box[nx][ny] == 'O':
            return OUT
        else:
            x, y = nx, ny
            steps += 1
        
def bfs(red, blue):
    queue = deque()
    visited = set()
    queue.append((red, blue, 0))
    visited.add((red[0], red[1], blue[0], blue[1]))
    
    while queue:
        red, blue, tilt = queue.popleft()
        if tilt >= 10:
            return -1
        
        for dir in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            move_red = move(red, dir)
            move_blue = move(blue, dir)
            
            # 공이 빠지는 경우
            if move_blue == OUT:
                continue
            if move_red == OUT:
                return tilt + 1
            
            # 같은 열 or 행에서 더 많이 이동한 쪽이 역방향 1개 이동
            new_red, new_blue = move_red[0], move_blue[0]
            steps_red, steps_blue = move_red[1], move_blue[1]
            if new_red == new_blue:
                if steps_red < steps_blue:
                    new_blue[0] -= dir[0]
                    new_blue[1] -= dir[1]
                else:
                    new_red[0] -= dir[0]
                    new_red[1] -= dir[1]
                        

            # 방문 체크
            state = (new_red[0], new_red[1], new_blue[0], new_blue[1])
            if state in visited:
                continue
            
            queue.append((new_red, new_blue, tilt + 1))
            visited.add(state)
        #if tilt + 1 > 10:
        #    return -1
    return -1   
print(bfs(red, blue))

'''
            # 같은 열 or 행에서 더 많이 이동한 쪽이 역방향 1개 이동
            # 행이동(dir : (1,0), (-1,0)) -> 같은 열일 경우
            # 열이동(dir : (0,1), (0,-1)) -> 같은 행일 경우
            # 역방향 이동 ? x-=dir[0] y-=dir[1]
            
            steps_red, steps_blue = move_red[1], move_blue[1]
            if steps_red < steps_blue:
                new_blue[0] -= dir[0]
                new_blue[1] -= dir[1]
            else:
                new_red[0] -= dir[0]
                new_red[1] -= dir[1]
'''