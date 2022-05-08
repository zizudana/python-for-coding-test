# 아기상어
from collections import deque
from gettext import ngettext

n = int(input()) # 공간의 크기 n
# 0 빈칸 / 1~6 물고기 / 9 아기상어
board = [list(map(int, input().split())) for _ in range(n)]

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(n):
	for j in range(n):
		if board[i][j] == 9: # 아기상어 좌표 (sx,sy)
			s_x = i 
			s_y = j

def bfs(s_x, s_y):
	visited = [[0] * n for _ in range(n)]
	queue = deque()
	queue.append((s_x, s_y))
	visited[s_x][s_y] = 1
	d = [[0] * n for _ in range(n)]
	eat = []
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = x + dy[i]
			if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
				if board[nx][ny] <= board[x][y] or board[nx][ny] == 0:
					queue.append((nx, ny))
					visited[nx][ny] = 1
					d[nx][ny] = d[x][y] + 1
				if board[nx][ny] != 0 and board[nx][ny] < board[x][y]:
					eat.append([nx, ny, d[nx][ny]])
	if not eat:
		return -1, -1, -1
	eat.sort(key = lambda x : (x[2], x[0], x[1]))
	return eat[0][0], eat[0][1], eat[0][2]


size = 0
cnt = 0
while True:
	x, y, d = bfs(s_x, s_y)
	if x == -1:
		break
	board[x][y] = board[s_x][s_y]
	board[s_x][s_y] = 0 # 상어가 지나간 자리 0으로
	size += 1
	if size == board[x][y]:
		size = 0
		board[x][y] += 1
	cnt += d
print(cnt)
