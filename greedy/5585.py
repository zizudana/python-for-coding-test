# https://www.acmicpc.net/problem/5585 거스름돈
n = int(input())
n = 1000 - n

result = 0
if n >= 500:
    result += (n // 500)
    n %= 500
if n >= 100:
    result += (n // 100)
    n %= 100
if n >= 50:
    result += (n // 50)
    n %= 50
if n >= 10:
    result += (n // 10)
    n %= 10
if n >= 5:
    result += (n //5)
    n %= 5
result += n
print(result)