# 백준 12904번 A와 B

S = input()
T = input()

STR = T
for _ in range(len(T)-len(S)):
    if STR[-1] == 'A':
        STR = STR[:-1]
    else:
        STR = STR[:-1][::-1]
if STR == S:
    print(1)
else:
    print(0)