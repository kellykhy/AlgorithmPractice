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
result = set()
for i in range(len(brackets)):
    for comb in combinations(brackets, i):
        cpy = input[:]
        for s, e in comb:
            cpy[s] = '('
            cpy[e] = ')'
        result.add(''.join(cpy))
result = sorted(result)
for i in result:
    print(i)