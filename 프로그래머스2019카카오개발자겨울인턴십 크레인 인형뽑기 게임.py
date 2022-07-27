# 프로그래머스 > 2019 카카오 개발자 겨울 인턴십 > 크레인 인형뽑기 게임

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    stacks = [[] for _ in range(len(board))]
    basket = []
    for row in board:
        for i in range(len(board)):
            if row[i]:
                stacks[i].insert(0, row[i])
    for move in moves:
        if len(stacks[move-1]):
            if len(basket) and (basket[-1] == stacks[move-1][-1]):
                answer += 2
                basket.pop()
                stacks[move-1].pop()
            else:
                basket.append(stacks[move-1].pop())
    return answer

print(solution(board, moves))