# 백준 2577번 숫자의 개수

mult = 1
for i in range(3):
    mult *= int(input())
str_mult = str(mult)

result = [0] * 10
for i in range(len(str_mult)):
    result[int(str_mult[i])] += 1

for i in range(10):
    print(result[i])