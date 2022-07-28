# 백준 2800번 괄호제거

from itertools import combinations

input = list(input())
stack = []
brackets = []
for i, j in enumerate(input):
    if j == '(':
        stack.append(i)
        input[i] = ''
    elif j == ')':
        brackets.append([stack.pop(), i])
        input[i] = ''

result = set() # 집합 자료형 : 중복 제거 # ((1)) -> (1), (1), 1 (3가지)
for i in range(len(brackets)):
    for comb in combinations(brackets, i): # 0, 1, 2, ... (n-1)개의 괄호쌍 조합
        cpy = input[:]
        for s, e in comb:
            cpy[s] = '('
            cpy[e] = ')'
        result.add(''.join(cpy))
result = sorted(result)
for i in result:
    print(i)