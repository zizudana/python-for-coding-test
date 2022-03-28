# 로봇청소기
import sys
input = sys.stdin.readline

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def clean(r, c, d):
  global cnt
  if board[r][c] == 0:  # 현재좌표가 청소할 수 있는지 확인
    board[r][c] = 2
    cnt += 1
  for i in range(4):
    nd = (d+3) % 4
    nx = r + dx[nd]
    ny = c + dy[nd]
    if (nx > 0 and ny > 0 and nx < n and ny < m):
      if board[nx][ny] == 0:  # 왼쪽으로 회전해서 청소할 수 있으면
       clean(nx, ny, nd)  #다음 좌표와 방향 입력
       return
    d = nd
  # 네 방향 모두 청소할 수 없는 경우
  nd = (d+2) % 4
  nx = r + dx[nd]
  ny = c + dx[nd]
  if board[nx][ny] == 1: # 뒤가 벽인 경우
    return
  clean(nx, ny, d) # 뒤로 이동할 수 있으면 다음좌표입력, 방향 유지

cnt = 0
clean(r, c, d)
print(cnt)
