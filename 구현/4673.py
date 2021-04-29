# https://www.acmicpc.net/problem/4673 셀프 넘버
num = [0] * 10001
def makeNum(n):
    result = n
    while n>= 10:
        result += (n % 10)
        n = (n // 10)
    return (result + n)


for i in range(100001):
    ino = makeNum(i)
    if ino < 10001:
        num[ino] = 1

for i in range(10001):
    if num[i] == 0:
        print(i)
