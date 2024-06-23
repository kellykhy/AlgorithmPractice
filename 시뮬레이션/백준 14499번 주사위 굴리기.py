# 백준 14499번 주사위 굴리기 (통과x)

import sys
input = sys.stdin.readline

N,M,x,y,K=map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
order_list = list(map(int, input().split()))
dice = [[0] * 3 for _ in range(4)] # 주사위

change_top = [[0,0], [0,-1], [0,1], [1,0], [-1,0]] # 윗면 x,동,서,북,남
change_position = [[0,0], [0,1], [0,-1], [-1,0], [1,0]]

def find_bottom(top):
    x,y = top[0],top[1]
    if (y == 1):
        return [(x+2)%4,y]
    else:
        return [x,(y+2)%4]

top = [1,1]
position = [0,0]
for order in order_list:
    dx, dy = change_top[order]
    dr, dc = change_position[order]
    if (position[0] + dr < 0 or position[0] + dr >= N or position[1] + dc < 0 or position[1] + dc >= M):
        print("pass")
        continue
    top[0] = (top[0] + dx) % 4
    top[1] = (top[1] + dy) % 4
    if (top[1] == 3):
        top = [3,1]
            
    position[0] += dr
    position[1] += dc
    bx, by = find_bottom(top)
    print("top = ", top, " bottom = ", "[", bx, ",", by, "]")
    print("position = ", position)
    tx, ty = top[0], top[1]
    if (graph[position[0]][position[1]] == 0):
        graph[position[0]][position[1]] = dice[bx][by]
    else:
        dice[bx][by] = graph[position[0]][position[1]]
        graph[position[0]][position[1]] = 0
        
    print(dice[tx][ty])