# 백준 1456번 거의 소수
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n = int(b ** 0.5) + 1

# 소수 구하기
prime = [1 for _ in range(n + 1)]
prime[0] = prime[1] = 0
for i in range(2, n//2+1):
    if prime[i]:
        x = i + i
        while (x <= n):
            prime[x] = 0
            x += i
# 거의 소수(소수의 N제곱)의 개수 구하기
result = 0
for i in range(2, n):
    if prime[i]:
        x = i * i
        while (x <= b):
            if (x >= a):
                result += 1
            x *= i
print(result)
