# https://www.acmicpc.net/problem/10162  전자레인지

a, b, c = 300, 60, 10
result = [0] * 3
T = int(input())
while True:
    if T >= a:
        result[0] += (T // a)
        T %= a
    if T >= b:
        result[1] += (T // b)
        T %= b
    if T >= c:
        result[2] += (T // c)
        T %= c
    if T < c:
        break
if T == 0:
    print(str(result[0]) + " " + str(result[1]) + " " + str(result[2]))
    # print(result[0], result[1], result[2])
    # print("{} {} {}".format(result[0], result[1], result[2]))
else:
    print(-1)