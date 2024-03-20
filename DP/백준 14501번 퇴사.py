# 백준 14501번 퇴사 (dp)

def bottom_up_dp(info, n):
    r = [0] * 25

    for i in range(n-1, -1, -1):
        days = info[i][0]
        pay = info[i][1]
        if (i + days <= n):
            r[i] = max(r[i+1], pay + r[days+i])
        else:
            r[i] = r[i+1]
    return r[0]
            

n = int(input())                     
info = []
for i in range(n):
    info.append(list(map(int, input().split()))) #[days, pay]

print(bottom_up_dp(info, n))
