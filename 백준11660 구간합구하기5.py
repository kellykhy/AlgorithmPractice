# 백준 11660번

n, m = list(map(int, input().split()))

matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
ranges = []
for i in range(m):
    one_range = list(map(int, input().split()))
    ranges.append(one_range)

print(matrix)
print(ranges)
