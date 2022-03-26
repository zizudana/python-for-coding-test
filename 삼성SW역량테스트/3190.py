# 뱀
import sys
from collections import deque
from time import time
input = sys.stdin.readline

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def change(c, nd):
  if c == 'L':  # 왼쪽으로 회전
    nd = (nd + 3) % 4
  else:  # 오른쪽으로 회전
    nd = (nd + 1) % 4
  return nd

def move():
  nt = 0  # 현재 시간 = 0
  nx, ny = 0, 0  # 현재 좌표
  nd = 1  # 현재 방향 = 1(오른쪽에서 시작)
  snake = deque([[0, 0]])  # 현재 뱀의 좌표
  
  while True:
    nt += 1
    nx += dx[nd]
    ny += dy[nd]

    # 방향을 바꿔야하는지 확인
    if nt in changes.keys(): 
      nd = change(changes[nt], nd)

    # 종료조건 확인
    if (nx < 0 or ny < 0 or nx >= n or ny >= n):
      break
    if ([nx, ny] in snake):
      break
    snake.append([nx, ny])  # 현 위치를 뱀 머리로
    if board[nx][ny] == 0: #사과가 없는 경우
      tx, ty = snake.popleft()  # 뱀 길이 감소
    elif board[nx][ny] == 1:  # 사과가 있는 경우
      board[nx][ny] = 0
  return nt

if __name__ == "__main__":
  n = int(input())
  k = int(input())
  board = [[0] * n for _ in range(n)]
  for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

  L = int(input())
  changes = {}
  for _ in range(L):
    x, c = input().split()
    changes[int(x)] = c

  print(move())





