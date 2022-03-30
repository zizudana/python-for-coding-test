# 연구소
from collections import deque
import copy
import sys
input = sys.stdin.readline

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
board = []
for i in range(n):
  board.append(list(map(int, input().split())))

def bfs():
  queue = deque()
  tmp = copy.deepcopy(board)
  for i in range(n):
    for j in range(m):
      if tmp[i][j] == 2:  # 바이러스가 있으면
        queue.append((i, j))  # 큐에 추가

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (nx >= 0 and ny >= 0 and nx < n and ny < m):
        if tmp[nx][ny] == 0:  # 빈칸이면
          tmp[nx][ny] = 2  # 바이러스 퍼짐
          queue.append((nx, ny))  # 큐에 추가

  cnt = 0
  global max_result
  for i in tmp:  # 안전영역 크기 계산
    for j in i:
      if j == 0:
        cnt += 1
  max_result = max(max_result, cnt)

def makewall(cnt):
  if cnt == 3:  # 벽을 3개 만들면 bfs수행
    bfs()
    return
  for i in range(n):
    for j in range(m):
      if board[i][j] == 0:
        board[i][j] = 1
        makewall(cnt + 1)
        board[i][j] = 0

max_result = 0
makewall(0)
print(max_result)