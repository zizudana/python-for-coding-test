# https://www.acmicpc.net/problem/1541 잃어버린 괄호
arr_m = input().split('-')
result = 0
for i in arr_m.pop(0).split('+'):
    result += int(i)

for i in arr_m:
    arr_p = i.split('+')
    for j in arr_p:
        result -= int(j)

print(result)
