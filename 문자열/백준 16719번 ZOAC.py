# 백준 16719번 ZOAC

import sys
input = sys.stdin.readline

word = input().rstrip()
word = [word[i] for i in range(len(word))]
selected = ['' for _ in range(len(word))]

def find_min(first, last):
    if (last - first) <= 0:
        return
    min_char = min(word[first:last])
    min_idx = first + word[first:last].index(min_char)
    selected[min_idx] = min_char
    print(''.join(selected))
    find_min(min_idx+1, last)
    find_min(first, min_idx)
    
find_min(0, len(word))
