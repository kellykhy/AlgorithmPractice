# 백준 15649번 N과 M(1)

def func(k):
    if (k==m):
        for i in range(m):
            print(arr[i], end = ' ')
        print()
        return
    for i in range(1, n+1):
        if (not isused[i]):
            arr[k] = i
            isused[i] = 1
            func(k+1)
            isused[i] = 0

n, m = map(int, input().split())
isused = [0] * (n+1)
arr = [0] * m
func(0)
