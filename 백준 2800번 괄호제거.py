# 백준 2800번 괄호제거

from itertools import combinations

input = list(input())
label = '@'
bracket = []
for i in range(len(input)):
    if input[i] == '(':
        label = chr(ord(label) + 1)
        input[i] = label
        bracket.append(label)
    elif input[i] == ')':
        input[i] = label
        label = chr(ord(label) - 1)

combs = []
for i in range(len(bracket)):
    combs += list(combinations(bracket, i+1))

result = []
for comb in combs:
    removed = ''.join([i for i in input if i not in comb])
    for c in bracket:
        if c not in comb:
            removed = removed.replace(c, '(', 1)
            removed = removed.replace(c, ')', 1)
    result.append(removed)
    
result = sorted(result)
for i in result:
    print(i)