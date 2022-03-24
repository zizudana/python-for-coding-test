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
      if (board[i][tail] != 0): # tail이 0이 아닐때
        tmp = board[i][tail] # tmp에 tail값을 저장해두고
        board[i][tail] = 0 # tail은 0으로 초기화
        if (board[i][head] == 0): 
          board[i][head] = tmp # head가 0이면 head에 tail값을 저장
        elif (board[i][head] == tmp): # head와 tail값이 같으면
          board[i][head] = board[i][head] + tmp # head에 tail값 더해서 저장 (head * 2)
          head = head + 1 # head++ -> 두번 합쳐지는 것 방지
        else: # head와 tail 값이 다르면
          head = head + 1 # head를 하나 옮기고
          board[i][head] = tmp # head에 tail값 넣기
      tail = tail + 1 # tail++
  return (board)

def move_down(board): # head, tail을 뒤에서 시작
  for i in range(n):
    head = n - 1
    tail = n - 2
    while (tail > -1):
      if (board[i][tail] != 0):
        tmp = board[i][tail]
        board[i][tail] = 0
        if (board[i][head] == 0):
          board[i][head] = tmp
        elif (board[i][head] == tmp):
          board[i][head] = board[i][head] + tmp
          head = head - 1
        else:
          head = head - 1
          board[i][head] = tmp
      tail = tail - 1
  return (board)

def move_left(board): # move_up과 거의 동일
  for i in range(n):
    head = 0
    tail = 1
    while (tail < n):
      if (board[tail][i] != 0):
        tmp = board[tail][i]
        board[tail][i] = 0
        if (board[head][i] == 0):
          board[head][i] = tmp
        elif (board[head][i] == tmp):
          board[head][i] = board[head][i] + tmp
          head = head + 1
        else:
          head = head + 1
          board[head][i] = tmp
      tail = tail + 1
  return (board)

def move_right(board): # move_down과 거의 동일
  for i in range(n):
    head = n - 1
    tail = n - 2
    while (tail > -1):
      if (board[tail][i] != 0):
        tmp = board[tail][i]
        board[tail][i] = 0
        if (board[head][i] == 0):
          board[head][i] = tmp
        elif (board[head][i] == tmp):
          board[head][i] = board[head][i] + tmp
          head = head - 1
        else:
          head = head - 1
          board[head][i] = tmp
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
