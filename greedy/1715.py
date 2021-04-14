# https://www.acmicpc.net/problem/1715 카드 정렬하기
# 골드문제...우선순위 큐를 이용해야함..다시풀기
n = int(input())
card = []
for _ in range(n):
    card.append(int(input()))
if len(card) > 1:
    card.sort()
    result = []
    result.append(card[0] + card[1])
    for i in range(2, n):
        result.append(result[i-2] + card[i])
    print(sum(result))
else:
    print(card[0])
