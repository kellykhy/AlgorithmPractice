# 백준 9663번 N-Queen

def func(k):
    global cnt
    if (k==n):
        cnt += 1
        return
    for i in range(n):
        if (k==0 or ((k+i) not in left_diag and (k-i) not in right_diag and i not in col)):
            left_diag.append(k+i)
            right_diag.append(k-i)
            col.append(i)
            func(k+1)
            left_diag.pop()
            right_diag.pop()
            col.pop()
            
def modified_func(k):
    global cnt
    if (k==n):
        cnt += 1
        return
    for i in range(n):
        if (k==0 or (not isused_ldiag[(k+i)] and not isused_rdiag[(k-i)+(n-1)] and not isused_col[i])):
            isused_ldiag[k+i] = 1
            isused_rdiag[(k-i)+(n-1)] = 1
            isused_col[i] = 1
            modified_func(k+1)
            isused_ldiag[k+i] = 0
            isused_rdiag[(k-i)+(n-1)] = 0
            isused_col[i] = 0

# 세번째 더 간단한 방법! -> isused 배열 대신 행렬로 체크함
# https://seongonion.tistory.com/103

cnt = 0
n = int(input())

#func
left_diag = []
right_diag = []
col = []

# modified func
isused_ldiag = [0] * (n+n+1)
isused_rdiag = [0] * (n+n-1) # -(N-1)=0 ... 0=(N-1) ... (N-1)=(2*N-2)
isused_col = [0] * (n+1)

#arr = []
modified_func(0)
print(cnt)