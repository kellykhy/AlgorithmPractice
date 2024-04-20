# 백준 1541번 잃어버린 괄호

import sys
input = sys.stdin.readline

equation = input().rstrip()
nums = []
ops = []

n = 0
num = ""
while (n < len(equation)):
    if (equation[n] == '-' or equation[n] == '+'):
        nums.append(int(num))
        ops.append(equation[n])
        num = ""
    else:
        num += equation[n]
    if (n == len(equation)-1):
        nums.append(int(num))
    n += 1

result = 0
bracket = 0
bopen = 0
for i, num in enumerate(nums):
    if (i == 0):
        result += num
        continue
    if (ops[i-1] == '-'):
        if (not bopen):
            bopen = 1
            bracket += num
        else:
            #bopen = 0
            result -= bracket
            #bopen = 1
            bracket = 0
            bracket += num
    elif (ops[i-1] == '+'):
        if (not bopen):
            result += num
        else:
            bracket += num
    if (i == len(nums)-1):
        if (bopen):
            result -= bracket

print(result)