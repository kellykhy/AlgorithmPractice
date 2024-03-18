# 백준 1629번 곱셈

a, b, c = map(int, input().split())

# 방법1
def func(a, b, c):
    #print("a = ", a, "b = ", b, "c = ", c)
    if (b == 1): # base condition
        return (a % c)
    elif (b % 2 == 0):
        return func(a, b//2, c) ** 2 % c
    else:
        return func(a, b-1, c) * a % c
    
# 방법2 -> 좀 더 효율적임.
def func1(a, b, c):
    #print("a = ", a, "b = ", b, "c = ", c)
    if (b == 1): # base condition
        return (a % c)
    val = func(a, b//2, c)
    val = val * val
    if (b % 2 == 0):
        return val % c
    else:
        return val * a % c
    
print(func1(a, b, c))
