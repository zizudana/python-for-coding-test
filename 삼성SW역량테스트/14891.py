# 톱니바퀴
import copy
import sys
input = sys.stdin.readline

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

mode = [
  [],
  [[0], [1], [2], [3]],
  [[0, 2], [1, 3]],
  [[0, 1], [1, 2], [2, 3], [0, 3]],
  [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
  [[0, 1, 2, 3]],
]
cctv_list = []
board = []
n, m = map(int, input().split())
for i in range(n):
  temp = list(map(int, input().split()))
  board.append(temp)
  for j in range(m):
    if temp[j] in [1,2,3,4,5]:
      cctv_list.append([temp[j], i, j]) # cctv종류, x좌표, y좌표

def cctv(board, tv, x, y):
  for i in tv:
    nx = x
    ny = y
    while True:
      nx += dx[i]
      ny += dy[i]
      if 0<=nx<n and 0<=ny<m:
        if board[nx][ny] == 0:
          board[nx][ny] = 7 # 감시한 영역은 7로바꾼다
        if board[nx][ny] == 6: 
          break
      else:
        break

def dfs(depth, board):
  global min_cnt
  if depth == len(cctv_list):
    cnt = 0
    for i in range(n):
      cnt += board[i].count(0)
    min_cnt = min(min_cnt, cnt)
    return
  temp = copy.deepcopy(board)
  cctv_mode, x, y = cctv_list[depth]
  for tv in mode[cctv_mode]:
    cctv(temp, tv, x, y)
    dfs(depth+1, temp)
    temp = copy.deepcopy(board)

min_cnt = 1e9
dfs(0, board)
print(min_cnt)