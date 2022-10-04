# 프로그래머스 단속카메라(한번에 통과)

def solution(routes):
    answer = len(routes)
    routes.sort(key=lambda x: x[0])
    for i in range(len(routes)-1):
        if routes[i][1] >= routes[i+1][0]:
            if routes[i][1] >= routes[i+1][1]: # case3(포함관계)
                answer -= 1
                routes[i+1] = [routes[i+1][0], routes[i+1][1]]
            else: # case1(겹침)
                answer -= 1
                routes[i+1] = [routes[i+1][0], routes[i][1]]
    return answer

    

# 테스트
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) # 2
print(solution([[-10,-10], [-5, -5]]))