# 백준 2104번 부분배열 고르기

N = int(input())
A = list(map(int, input().split())) # [(0,3), (1,1), (2,6) ... (5,2)]
A = list(enumerate(A))

CS = [] #누적합 저장
cum_sum = 0
for (i,n) in A:
    cum_sum += n
    CS.append(cum_sum)

i_j = []
index = []
A.sort(key = lambda x: x[1])
for (idx,n) in A:
    i, j = A[0][0], A[0][0]
    for j in range(len(index)-1):
        if index[j]>idx:
            
        if (index[j]<idx and index[j+1]>idx):
            i = index[j]
            j = index[j+1]-1
    index.append(idx)
    i_j.append([i,j])

                
    index.append(i)