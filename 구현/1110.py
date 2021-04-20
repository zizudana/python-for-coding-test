# https://www.acmicpc.net/problem/1110 더하기 사이클
"""
(시간초과)
n = input()
new_n = n
cnt = 0
while True:
    cnt += 1
    if len(new_n) == 1:
        new_n = new_n * 2
    else:
        num = str(int(new_n[0]) + int(new_n[1]))
        new_n = new_n[1] + num[-1]
    if new_n == n:
        break
print(cnt)
"""
n = int(input())
new_n = n
cnt = 0

while True:
    a = new_n // 10
    b = new_n % 10
    c = (a+b) % 10
    new_n = (b * 10) + c
    cnt += 1
    if new_n == n:
        break
print(cnt)