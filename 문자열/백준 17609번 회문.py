# 백준 17609번 회문

import sys
input = sys.stdin.readline


def checkPalindrome():
    n = int(input().rstrip())
    result = [2] * n
    for i in range(n):
        word = input().rstrip()
        if (word[::] == word[::-1]):
            result[i] = 0
        else:
            s = 0
            e = len(word) -1
            while (s <= e):
                if (word[s] == word[e]):
                    s += 1
                    e -= 1
                else:
                    if (word[s+1] == word[e]):
                        temp = word[:s] + word[s+1:]
                        if (temp[::] == temp[::-1]):
                            result[i] = 1
                    if (word[s] == word[e-1]):
                        temp = word[:e] + word[e+1:]
                        if (temp[::] == temp[::-1]):
                            result[i] = 1
                    break
                
    return result

if __name__ == "__main__":
    print(*checkPalindrome(), sep='\n')
