# 백준 1926번 그림

import sys

def bfs(x, y):
    queue = []
    queue.insert(0, (i, j)) # a 큐에 넣기
    my_map[i][j] = 0 # b 방문 표시
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    w = 1 # 그림의 넓이
    while queue:
        x,y = queue.pop()

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if (new_x < 0 or new_x >= n or new_y < 0 or new_y >= m):
                continue
            if (my_map[new_x][new_y] == 0):
                continue
            queue.insert(0, (new_x, new_y)) # a 큐에 넣기
            my_map[new_x][new_y] = 0 # b 방문 표시
            w += 1
    width.append(w)
            

#input     
n, m = map(int, sys.stdin.readline().split())
my_map = []
for i in range(n):
    row = list(map(int, input().split()))
    my_map.append(row)

result = 0
width = [0]
for i in range(n):
    for j in range(m):
        if (my_map[i][j] == 1): # 아직 방문 안 했고, 방문 가능하면(범위 내이면)
            result += 1
            bfs(i, j)
            
            
print(result) # 그림의 개수
print(max(width)) # 제일 넓이가 큰 그림의 넓이


'''
수정해볼 부분1. (수정 완료)

전제) 이미 방문했거나 그림이 아닌 영역이면 방문하면 안됨.

1) vis -> 방문헀는지 체크 (방문했으면 1, 아니면 0)
2) my_map -> 그림인지 아닌지 체크 (그림이면 1, 아니면 0) (소위 길이 있는지 아닌지 체크하는 것과 동일)

=> 이 두개를 하나로 합칠 수 있음. 
=> HOW? 방문했는지 체크하는 부분(vis) -> my_map 값을 0으로 바꿈으로서 방문하면 안되는 영역으로 표시하면 됨.
'''

'''
수정해볼 부분2. (수정 완료)

< input() vs sys.stdin.readline() >
차이점?
- input()은 매개변수로 prompt message를 받는다. & 입력받은 개행 문자를 삭제시키고 반환한다.(즉, 입력받는 값 하나하나를 버퍼에 저장)
- sys.stdin.readline()은 개행문자 "\n"를 같이 입력받는다. -> 더 빠름 (대신 split()을 쓰지 않을 때는 개행문자 신경 써줘야함)

=> input() -> sys.stdin.readline()
'''
