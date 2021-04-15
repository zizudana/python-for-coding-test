# https://www.acmicpc.net/problem/1339 단어 수학
# 골드문제....나중에 다시 도전
n = int(input())
dic_word = {}
for _ in range(n):
    word = input()
    for i in range(len(word)):
        w = word[i]
        if w in dic_word:
            dic_word[w] += 10 ** (len(word)-i-1)
        else:
            dic_word[w] = 10 ** (len(word)-i-1)

nums = []
for value in dic_word.values():
    nums.append(value)
nums.sort(reverse=True)
result = 0
cnt = 9
for i in nums:
    result += (i*cnt)
    cnt -= 1
print(result)
