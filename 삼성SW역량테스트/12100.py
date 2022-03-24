# 2048 (Easy)
import sys
import copy

n = int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range (n)]

def move_up(board):
  for i in range(n):
    head = 0
    tail = 1
    while (tail < n):
      if (board[i][tail] != 0):
        if (board[i][head] == 0):
          board[i][head] = board[i][tail]
          board[i][tail] = 0
        elif (board[i][head] == board[i][tail]):
          board[i][head] = board[i][head] + board[i][tail]
          board[i][tail] = 0
        else:
          head = head + 1
          if (head != tail):
            board[i][head] = board[i][tail]
            board[i][tail] = 0
      tail = tail + 1
  return (board)

def move_down(board):
  for i in range(n):
    head = n - 1
    tail = n - 2
    while (tail > -1):
      if (board[i][tail] != 0):
        if (board[i][head] == 0):
          board[i][head] = board[i][tail]
          board[i][tail] = 0
        elif (board[i][head] == board[i][tail]):
          board[i][head] = board[i][head] + board[i][tail]
          board[i][tail] = 0
        else:
          head = head - 1
          if (head != tail):
            board[i][head] = board[i][tail]
            board[i][tail] = 0
      tail = tail - 1
  return (board)

def move_left(board):
  for i in range(n):
    head = 0
    tail = 1
    while (tail < n):
      if (board[tail][i] != 0):
        if (board[head][i] == 0):
          board[head][i] = board[tail][i]
          board[tail][i] = 0
        elif (board[head][i] == board[tail][i]):
          board[head][i] = board[head][i] + board[tail][i]
          board[tail][i] = 0
        else:
          head = head + 1
          if (head != tail):
            board[head][i] = board[tail][i]
            board[tail][i] = 0
      tail = tail + 1
  return (board)

def move_right(board):
  for i in range(n):
    head = n - 1
    tail = n - 2
    while (tail > -1):
      if (board[tail][i] != 0):
        if (board[head][i] == 0):
          board[head][i] = board[tail][i]
          board[tail][i] = 0
        elif (board[head][i] == board[tail][i]):
          board[head][i] = board[head][i] + board[tail][i]
          board[tail][i] = 0
        else:
          head = head - 1
          if (head != tail):
            board[head][i] = board[tail][i]
            board[tail][i] = 0
      tail = tail - 1
  return (board)

def dfs(cnt, board):
  global ans
  if (cnt == 5):
    for i in range(n):
      ans = max(ans, max(board[i]))
    return
  else:
    dfs(cnt + 1, move_up(copy.deepcopy(board)))
    dfs(cnt + 1, move_down(copy.deepcopy(board)))
    dfs(cnt + 1, move_left(copy.deepcopy(board)))
    dfs(cnt + 1, move_right(copy.deepcopy(board)))

ans = 0
if (n == 1):
  ans = board[0][0]
else:
  dfs(0, board)
print(ans)
