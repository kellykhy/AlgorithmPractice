# 백준 1003번 피보나치 함수

def fibonacci(n, count):
    if n in count:
        print(count[n][0], count[n][1])
        return
    for i in range(2,n+1):
        zero = count[i-1][0] + count[i-2][0]
        one = count[i-1][1] + count[i-2][1]
        count[i] = [zero, one]
    print(count[n][0], count[n][1])

count = {0: [1,0], 1: [0,1]}
fibo = [0, 1]
t = int(input())
t_cases = []
for i in range(t):
    t_cases.append(int(input()))
for case in t_cases:
    fibonacci(case, count)