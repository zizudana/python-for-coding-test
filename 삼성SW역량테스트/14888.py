# 연산자 끼워넣기
n = int(input())
a_list = list(map(int, input().split()))
op = list(map(int, input().split()))

def dfs(depth, num):
  global min_num
  global max_num
  if depth == n:
    max_num = max(num, max_num)
    min_num = min(num, min_num)
    return
  else:
    for i in range(4):
      if op[i] > 0:
        op[i] -= 1
        if i == 0:
          dfs(depth+1, num+a_list[depth])
        elif i == 1:
           dfs(depth+1, num-a_list[depth])
        elif i == 2:
          dfs(depth+1, num*a_list[depth])
        elif i == 3:
          dfs(depth+1, int(num/a_list[depth]))
        op[i] += 1

min_num = 1e9
max_num = -1e9
dfs(1, a_list[0])
print(max_num)
print(min_num)