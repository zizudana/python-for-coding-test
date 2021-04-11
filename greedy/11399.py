# https://www.acmicpc.net/problem/11399 ATM
import sys

n = int(input())
arr_p = list(map(int, sys.stdin.readline().split()))
arr_p.sort()

sum1 = 0
sum2 = 0
for p in arr_p:
    sum1 += p
    sum2 += sum1

print(sum2)