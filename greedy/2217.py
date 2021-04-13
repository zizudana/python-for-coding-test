# https://www.acmicpc.net/problem/2217 로프
n = int(input())
arr_num = []
for _ in range(n):
    arr_num.append(int(input()))
arr_num.sort(reverse=True)
result = []
for i in range(n):
    result.append(arr_num[i] * (i+1))

print(max(result))