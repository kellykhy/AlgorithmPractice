# 백준 11729번 하노이 탑 이동 순서

def hanoi(n, depart, arrive, bypass):
    if n == 1:
        print(depart, arrive)
    else:
        hanoi(n-1, depart, bypass, arrive)
        print(depart, arrive)
        hanoi(n-1, bypass, arrive, depart)

k = int(input())
print((1<<k) - 1)
hanoi(k, 1, 3, 2)