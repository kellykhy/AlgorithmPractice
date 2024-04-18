# 백준 7785번 회사에 있는 사람

import sys
input = sys.stdin.readline

n = int(input())
log_list = dict()
for _ in range(n):
    name, status = list(input().split())
    log_list[name] = 1 if status == "enter" else 0

result = []
for key, value in log_list.items():
    if (value == 1):
        result.append(key)
result.sort(reverse = True)
for i in range(len(result)):
    print(result[i])