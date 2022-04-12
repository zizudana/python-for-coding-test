# 드래곤 커브
import sys
input = sys.stdin.readline

# 방향 0 1 2 3
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input()) # 드래곤 커브의 개수
board = [[0] * 101 for _ in range(101)] # 격자 0으로 초기화
for i in range(n):
  x, y, d, g = map(int, input().split()) # 시작좌표(x, y), 시작방향 d, 세대 g
  board[x][y] = 1 # 시작좌표를 1로
  que = [d] # 방향큐에 시작방향을 넣는다
  for _ in range(g):
    for q in range(len(que)-1, -1, -1):
      que.append((que[q]+1)%4) # 맨 뒤부터 방향+1한것을 방향큐에 추가
  for q in que:
    x += dx[q]
    y += dy[q]
    board[x][y] = 1

result = 0
for i in range(100):
  for j in range(100):
    if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
      result += 1
print(result)

