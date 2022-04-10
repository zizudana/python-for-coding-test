# 경사로
import sys
input = sys.stdin.readline

n, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def check(line):
  ramp = [0 for _ in range(n)] # 경사로를 놓으면 1, 아니면 0
  for i in range(n-1):
    if line[i] == line[i+1]:
      continue
    if abs(line[i] - line[i+1]) > 1: # 높이차가 1보다 크면 false
      return False
    if line[i] > line[i+1]: # 이전 높이가 더 클때
      temp = line[i+1]
      for j in range(i+1, i+1+L):
        if 0<=j<n:
          if (line[j] != temp) or (ramp[j] == 1):
            return False
          ramp[j] = 1 # 경사로를 놓는다
        else:
          return False
    else: # 다음 높이가 더 클때
      temp = line[i]
      for j in range(i, i-L, -1):
        if 0<=j<n:
          if (line[j] != temp) or (ramp[j] == 1):
            return False
          ramp[j] = 1
        else:
          return False
  return True

cnt = 0
for line in board:
  if check(line):
    cnt += 1
for i in range(n):
  line = []
  for j in range(n):
    line.append(board[j][i])
  if check(line):
    cnt += 1
print(cnt)

