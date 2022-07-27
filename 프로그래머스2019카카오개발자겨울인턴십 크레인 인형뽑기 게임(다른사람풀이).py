# 프로그래머스 > 2019 카카오 개발자 겨울 인턴십 > 크레인 인형뽑기 게임(다른 사람 풀이)

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    basket = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]:
                basket.append(board[j][i-1])
                board[j][i-1] = 0

                if len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        basket.pop()
                        basket.pop()
                        answer += 2
                break

    return answer

print(solution(board, moves))