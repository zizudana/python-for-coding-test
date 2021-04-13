# https://www.acmicpc.net/problem/1946 신입 사원
import sys

ex = int(input())
for _ in range(ex):
    arr_n = []
    n = int(input())
    count = 1
    for _ in range(n):
        arr_n.append(list(map(int, sys.stdin.readline().split())))
    arr_n.sort()
    min_n = arr_n[0][1]
    for ar in arr_n:
        if ar[1] < min_n:
            count += 1
            min_n = ar[1]
    print(count)
