# 백준 10808번 알파벳 개수

# ord("a") == 97
S = input()
result = [0] * 26
for i in range(len(S)):
    result[ord(S[i])-ord("a")] += 1

for i in result:
    print(i, end = ' ')