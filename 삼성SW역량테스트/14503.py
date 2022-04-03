# 로봇청소기
import sys
input = sys.stdin.readline

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split()) # n * m 직사각형
r, c, d = map(int, input().split()) # 좌표(r, c) , 방향 d
board = [list(map(int, input().split())) for _ in range(n)] # 빈칸 0, 벽 1

def clean(r, c, d):
  global cnt # 청소한 칸의 개수
  if board[r][c] == 0:  # 현재좌표가 청소할 수 있는지 확인
    board[r][c] = 2
    cnt += 1
  for _ in range(4):
    nd = (d+3) % 4 # 왼쪽 방향으로 회전
    nx = r + dx[nd]
    ny = c + dy[nd]
    if board[nx][ny] == 0:  # 왼쪽으로 이동해서 청소할 수 있으면
      clean(nx, ny, nd)  #다음 좌표와 방향 입력
      return
    d = nd
  # 네 방향 모두 청소할 수 없는 경우
  nd = (d+2) % 4 # 방향을 뒤로
  nx = r + dx[nd]
  ny = c + dy[nd]
  if board[nx][ny] == 1: # 뒤가 벽인 경우
    return
  clean(nx, ny, d) # 뒤로 이동할 수 있으면 방향 유지한채로 이동

cnt = 0
clean(r, c, d)
print(cnt)
