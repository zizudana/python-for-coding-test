# input
m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

dx = [1, 0, 1]
dy = [0, 1, 1]

answer = 0
for i in range(len(board)):
  board[i] = list(board[i])

while True:
  remove = [[0]*n for _ in range(m)]
  for i in range(m-1):
    for j in range(n-1):
      if board[i][j] != 0:
        for d in range(3):
          if board[i][j] != board[i+dx[d]][j+dy[d]]:
            break
        else:
          remove[i][j] = 1
          for d in range(3):
            remove[i+dx[d]][j+dy[d]] = 1
  cnt = 0
  for i in range(m):
    cnt += sum(remove[i])
  answer += cnt
  if cnt == 0:
    break
  for i in range(m-1, -1, -1):
    for j in range(n):
      if remove[i][j] == 1:
        x = i-1
        while(x>=0 and remove[x][j] == 1):
          x -= 1
        if x<0:
          board[i][j] = 0
        else:
          board[i][j] = board[x][j]
          remove[x][j] = 1
print(answer)