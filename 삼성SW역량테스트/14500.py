# 테트로미노
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, depth, result):
  global max_result
  if depth == 4:
    max_result = max(max_result, result)
    return 
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if (0<=nx<n and 0<=ny<m and visited[nx][ny] == 0):
      if depth == 2:
        visited[nx][ny] = 1
        dfs(x, y, depth+1, result+board[nx][ny])
        visited[nx][ny] = 0
      visited[x][y] = 1
      dfs(nx, ny, depth+1, result+board[nx][ny])
      visited[nx][ny] = 0

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
max_result = 0
for i in range(n):
  for j in range(m):
    visited[i][j] = 1
    dfs(i, j, 1, board[i][j])
    visited[i][j] = 0
print(max_result)

