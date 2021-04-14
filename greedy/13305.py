# https://www.acmicpc.net/problem/13305 주유소
import sys

n = int(input())
length = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

min_p = price[0]
cost = length[0] * price[0]
for i in range(1, n-1):
    if price[i] < min_p:
        min_p = price[i]
    cost += (min_p * length[i])
print(cost)