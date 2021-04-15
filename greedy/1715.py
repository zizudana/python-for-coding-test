# https://www.acmicpc.net/problem/1715 카드 정렬하기
# 골드문제...우선순위 큐를 이용해야함..다시풀기
import heapq
import sys

n = int(input())
card = []
for _ in range(n):
    heapq.heappush(card, int(sys.stdin.readline()))

if len(card) > 1:
    result = 0
    while len(card) > 1:
        temp_1 = heapq.heappop(card)  # 가장 작은 덱
        temp_2 = heapq.heappop(card)  # 두번째로 작은 덱
        result += (temp_1 + temp_2)
        heapq.heappush(card, temp_1 + temp_2)
    print(result)
else:
    print(0)
