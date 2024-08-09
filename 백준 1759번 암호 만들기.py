# 백준 1759번 암호 만들기

import sys
from copy import deepcopy

input = sys.stdin.readline

def select_consonant(cnum, k, combination):
    if (k == cnum):
        combinations.append(sorted(deepcopy(combination)))
        return
    for i in range(len(consonants)):
        if visited_c[i]:
            continue
        if (len(combination) - l + cnum) and (combination[-1] > consonants[i]): #중복 방지
            continue
        combination.append(consonants[i])
        visited_c[i] = 1
        select_consonant(cnum, k+1, combination)
        combination.pop()
        visited_c[i] = 0

def select_vowel(vnum, k, combination):
    if (k == vnum):
        select_consonant(l-vnum, 0, combination)
        return
    for i in range(len(vowels)):
        if visited_v[i]:
            continue
        if len(combination) and (combination[-1] > vowels[i]): #중복 방지
            continue
        combination.append(vowels[i])
        visited_v[i] = 1
        select_vowel(vnum, k+1, combination)
        combination.pop()
        visited_v[i] = 0


l, c = map(int, input().split())
letters = list(input().split())
vowels = []
consonants = []

for letter in letters:
    if letter in ('a', 'e', 'i', 'o', 'u'):
        vowels.append(letter)
    else:
        consonants.append(letter)
vowels.sort()
consonants.sort()

combinations = []
for i in range(1, (l-2) + 1):
    visited_v = [0 for _ in range(len(vowels))]
    visited_c = [0 for _ in range(len(consonants))]
    select_vowel(i, 0, [])

combinations.sort()
for comb in combinations:
    print(''.join(comb))