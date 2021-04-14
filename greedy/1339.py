# https://www.acmicpc.net/problem/1339 단어 수학
# 골드문제....나중에 다시 도전
n = int(input())
arr_word = []
for _ in range(n):
    word = input()
    arr_word.append(len(word), word)
arr_word.sort()
for word in arr_word:
    n9 = word[1][0]