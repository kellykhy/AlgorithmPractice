# 파괴되지 않은 건물

def solution(board, skill):
    answer = 0
    tmp = [[0 for i in range(len(board[0])+1)] for j in range(len(board)+1)]
    for (type, r1, c1, r2, c2, degree) in skill:
        tmp[r1][c1] += degree if type == 2 else -degree
        tmp[r1][c2+1] -= degree if type == 2 else -degree
        tmp[r2+1][c1] -= degree if type == 2 else -degree
        tmp[r2+1][c2+1] += degree if type == 2 else -degree
        
    # 행 기준 누적합
    for i in range(len(tmp)):
        for j in range(1,len(tmp[0])):
            tmp[i][j] += tmp[i][j-1]
    # 열 기준 누적합
    for i in range(1,len(tmp)):
        for j in range(len(tmp[0])):
            tmp[i][j] += tmp[i-1][j]
            
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += tmp[i][j]
            if (board[i][j] >= 1):
                print("%d %d" %(i,j))
                answer+=1
    return answer



board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]	
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))


'''
for i in range(len(board)):
        for j in range(len(board[0])):
            print("%2d" %board[i][j], end = ' ')
        print()
        '''
