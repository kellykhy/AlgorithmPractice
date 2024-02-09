# 백준 1475번 방 번호

N = input()
need = [0] * 10
for i in range(len(N)):
    n = int(N[i])
    need[n] += 1
need[6] = (need[6] + need[9] +1) // 2
need[9] = need[6]
print(max(need))

# 1 set needed (1~2개) 2 3
# 2 sets needed (3~4개) 4 5
# 3 sets needed (5~6개) 6 7



