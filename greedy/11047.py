# https://www.acmicpc.net/problem/11047 동전 0
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

result = 0
for i in reversed(coins):
    if k < i:
        continue
    else:
        result += (k // i)
        k = k % i
        if k == 0:
            break
print(result)



