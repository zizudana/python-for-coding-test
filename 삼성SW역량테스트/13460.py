# 구슬 탈출 2
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for i in range(n):
  board.append(list(input().rstrip()))
  for j in range(m):
    if board[i][j] == 'R':
      rx, ry = i, j  # 빨간구슬 좌표 rx, ry
    elif board[i][j] == 'B':
      bx, by = i, j

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, dx, dy):
  cnt = 0
  while True:
    if (board[x+dx][y+dy] == '#' or board[x+dx][y+dy] == '0'):
      break
    x += dx
    y += dy
    cnt += 1
  return (x, y, cnt)

def bfs(rx, ry, bx, by):
  queue = deque()
  queue.append((rx, ry, bx, by))
  visited = []
  visited.append((rx, ry, bx, by))
  cnt = 0
  while (queue and cnt < 10):
    cnt += 1
    rx, ry, bx, by = queue.popleft()
    for i in range(4):
      nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
      nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
      if board[nbx][nby] != 'O':
        if board[nrx][nry] == 'O':
          print(cnt)
          return
        if nrx == nbx and nry == nby:
          if rcnt > bcnt:
            nrx -= dx[i]
            nry -= dy[i]
          else:
            nbx -= dx[i]
            nby -= dy[i]
        if (nrx, nry, nbx, nby) not in visited:
          visited.append((nrx, nry, nbx, nby))
          queue.append((nrx, nry, nbx, nby))
  print(-1)

bfs(rx, ry, bx, by)