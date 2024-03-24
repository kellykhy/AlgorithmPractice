# 백준 3273번 두 수의 합

# input
n = int(input())
num_list = list(map(int, input().split()))
x = int(input())

result = 0
ary = [0 for _ in range(1000001)]
for num in num_list:
    if (x - num > 0 and x - num < 1000001 and ary[x - num] > 0):
        result += 1
    ary[num] += 1

print(result)

# example
# n = 5
# 2 4 6 9 15
# x = 12
