# 백준 1074번 Z

def func(N, r, c): # 내 풀이
    if (N==1):
        return 2*r+1*c
    r1 = r // (2**(N-1))
    c1 = c // (2**(N-1))
    r2 = r % (2**(N-1))
    c2 = c % (2**(N-1))
    return 4**(N-1)*(2*r1+c1) + func(N-1, r2, c2)

def func2(N, r, c): # 강사 풀이
    if (N==0):
        return 0
    half = 1<<(N-1) # 2**(N-1)
    if (r < half and c < half): return func(N-1, r, c) # (0,0) 사각형 [가장 큰 범위에서의 위치]
    if (r < half and c >= half): return half*half+func(N-1, r, c-half) # (0,1) 사각형
    if (r >= half and c < half): return 2*half*half+func(N-1, r-half, c) # (1,0) 사각형
    return 3*half*half+func(N-1, r-half, c-half) #(1,1) 사각형
    
    
N, r, c = map(int, input().split())
print(func(N, r, c))