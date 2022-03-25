# 주사위 굴리기
import sys
input = sys.stdin.readline

# 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, m, x, y, k = map(int, input().split())
board = []
for _ in range(n):
  board.append(list(map(int, input().split())))
move_list = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0] # 1(윗면),2,3,4,5,6(바닥면)

def move(i):
  d0, d1, d2, d3, d4, d5 = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
  if i == 1: # 동
    dice[0], dice[2], dice[3], dice[5] = d3, d0, d5, d2
  if i == 2: # 서
    dice[0], dice[2], dice[3], dice[5] = d2, d5, d0, d3
  if i == 3: # 북
    dice[0], dice[1], dice[4], dice[5] = d4, d0, d5, d1
  if i == 4: # 남
    dice[0], dice[1], dice[4], dice[5] = d1, d5, d0, d4

nx, ny = x, y
for i in move_list:
  nx += dx[i-1]
  ny += dy[i-1]
  if (nx < 0 or ny < 0 or nx >= n or ny >= m): # 지도를 벗어나는 경우
    nx -= dx[i-1]
    ny -= dy[i-1]
    continue # 다시 되돌리고 넘어가기
  move(i)
  if board[nx][ny] == 0: # 이동한 칸의 수가 0이면
    board[nx][ny] = dice[5] # 주사위 바닥면의 수를 칸에 복사
  else: # 이동한 칸의 수가 0이 아니면
    dice[5] = board[nx][ny] # 칸에 쓰인 수를 주사위 바닥면에 복사
    board[nx][ny] = 0 # 칸에 쓰인 수는 0으로
  print(dice[0])
