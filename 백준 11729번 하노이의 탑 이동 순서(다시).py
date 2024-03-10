# 백준 11729번 하노이의 탑 이동 순서

def hanoi(n, start, past, dest):
    if (n==1):
        print(start, dest)
    else:
        hanoi(n-1, start, dest, past)
        print(start, dest)
        hanoi(n-1, past, start, dest)

K = int()
hanoi(K, 1, 2, 3)