# https://www.acmicpc.net/problem/2750 수 정렬하기
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
array.sort()
for i in range(n):
    print(array[i])