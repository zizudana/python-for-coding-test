# 인구 이동
from collections import deque
import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, L, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def bfs(i, j):
	queue = deque()
	queue.append((i, j))
	visited[i][j] = 1
	union = []
	union.append((i, j))
	temp = board[i][j]
	cnt = 1

	while (queue):
		x, y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if (0<=nx<n and 0<=ny<n and not visited[nx][ny]):
				if (L <= abs(board[x][y] - board[nx][ny]) <= r):
					visited[nx][ny] = 1
					queue.append((nx, ny))
					temp += board[ny][ny]
					cnt += 1
					union.append((nx, ny))
	temp = temp // cnt
	if cnt > 1:
		for x, y in union:
			board[x][y] = temp
	return cnt

# 0,0부터 n,n까지 bfs를 돌리고 인구이동이 발생했으면 다시 0,0부터 bfs를 돌림
# 이동이 발생하지 않았으면 멈춤
result = 0
while True:
	flag = 0
	visited = [[0] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			if not visited[i][j]:
				if bfs(i, j) > 1:
					result += 1
	else:
		break
print(result)
