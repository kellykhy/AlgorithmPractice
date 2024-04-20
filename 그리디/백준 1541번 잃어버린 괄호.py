# 백준 1541번 잃어버린 괄호

import sys
input = sys.stdin.readline

equation = input().rstrip()
parts = equation.split('-')

result = 0
nums = []
for part in parts:
    sum = 0
    for p in part.split('+'):
        sum += int(p)
    nums.append(sum)
    
result += nums[0]
for i in range(1, len(nums)):
    result -= nums[i]
        
print(result)