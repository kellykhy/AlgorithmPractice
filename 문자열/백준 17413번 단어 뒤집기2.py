# 백준 17413번 단어 뒤집기2

import sys
input = sys.stdin.readline().rstrip

S = input()
flag = 0
wordStacks = []
reverse_S = []
i = 0
while (i < len(S)):
    if (S[i] == '<'): 
        flag = 1
    if (flag == 1):
        reverse_S += S[i]
        if (S[i] == '>'):
            flag = 0
        i += 1
    elif (S[i] == ' '):
        reverse_S += S[i]
        i += 1
    else:
        wordStack = []
        while (i < len(S) and S[i] != ' ' and S[i] != '<'):
            reverse_S += '*'
            wordStack.append(S[i])
            i += 1
        wordStacks.append(wordStack)

flag = 0
for i in range(len(reverse_S)):
    if (len(wordStacks) > 0 and len(wordStacks[0]) == 0):
        wordStacks.pop(0)
    if (S[i] == '<'):
        flag = 1
    if (reverse_S[i] == '*'):
        reverse_S[i] = wordStacks[0].pop()
    if (S[i] == '>'):
        flag = 0

print(''.join(reverse_S))
