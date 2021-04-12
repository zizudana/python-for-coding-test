# https://www.acmicpc.net/problem/1931 회의실 배정
import sys

n = int(input())
arr_c = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr_c.append((a, b))

arr_c.sort(key=lambda x: (x[1], x[0]))

result = []
endtime = 0
for a, b in arr_c:
    if a >= endtime:
        result.append((a, b))
        endtime = b

print(len(result))
