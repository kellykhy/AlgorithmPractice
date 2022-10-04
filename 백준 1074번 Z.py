# 백준 1074번 Z

def ftn(N, r, c):
    add = 0
    if (1<<(N-1) > r):
        if (1<<(N-1) <= c):
            add += (1<<(N-1)*2)
    else:
        if (1<<(N-1) > c):
            add += 2*(1<<(N-1)*2)
        else:
            add += 3*(1<<(N-1)*2)
    return add

N, r, c = map(int, input().split())
result = 0
while (N):
    result += ftn(N,r,c)
    r %= (1<<(N-1))
    c %= (1<<(N-1))
    N -= 1
print(result)