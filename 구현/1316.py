# https://www.acmicpc.net/problem/1316 그룹 단어 체커
n = int(input())
array = []
for i in range(n):
    array.append(input())


def isGroup(st):
    ar = []
    flag = 0
    for i in range(len(st)-1):
        if st[i] != st[i+1]:
            if st[i+1] in ar:
                flag = 1
                break
            ar.append(st[i])
    if flag:
        return 0
    else:
        return 1

count = 0
for i in array:
    count += isGroup(i)

print(count)
