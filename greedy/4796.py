# https://www.acmicpc.net/problem/4796 캠핑
i = 0
while True:
    i += 1
    l, p, v = map(int, input().split())
    if l == 0:
        break
    result = (v // p) * l
    result += min(v % p, l)
    print("Case %d: %d" % (i, result))
