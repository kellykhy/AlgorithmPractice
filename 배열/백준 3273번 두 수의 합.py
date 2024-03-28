# 백준 3273번 두 수의 합
'''
import sys
input = sys.stdin.readline

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
'''
import sys
input = sys.stdin.readline

n = int(input())
ary = list(map(int, input().split()))
x = int(input())

ary.sort()
p1, p2 = 0, n-1
ans = 0
while (p1 < p2):
    if (ary[p1] + ary[p2] < x):
        p1 += 1
    elif (ary[p1] + ary[p2] > x):
        p2 -= 1
    else:
        ans += 1
        p1 += 1
        p2 -= 1
print(ans)
        
    

# example
# n = 5
# 2 4 6 9 15
# x = 12
