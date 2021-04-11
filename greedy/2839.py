# https://www.acmicpc.net/problem/2839 설탕 배달
n = int(input())

result = 0
flag = False
while n >= 0:
    if n % 5 == 0:
        result += (n // 5)
        print(result)
        flag = True
        break
    n -= 3
    result += 1

if not flag:
    print(-1)
