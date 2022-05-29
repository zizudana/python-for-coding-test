# 상어 초등학교

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
student = []
# 학생번호, 좋아하는 학생번호 4개
for _ in range(n**2):
	student.append(list(map(int, input().split())))
board = [[0] * n for _ in range(n)] # n * n

for s in student:
	tmp = []
	for i in range(n):
		for j in range(n):
			if not board[i][j]:
				like = 0 # 인접하는 좋아하는 학생 수
				empty = 0 # 인접하는 빈자리 수
				for ii in range(4):
					nx = i + dx[ii]
					ny = j + dy[ii]
					if 0<=nx<n and 0<=ny<n:
						if board[nx][ny] in s[1:]: # 좋아하는 학생
							like += 1
						if not board[nx][ny]: # 빈자리
							empty += 1
				tmp.append((like, empty, i, j))
	# 좋아하는학생이 많은 순 -> 빈자리가 많은 순-> 행번호 작은 순-> 열번호 작은 순
	tmp.sort(key = lambda x:(-x[0] , -x[1], x[2], x[3]))
	board[tmp[0][2]][tmp[0][3]] = s[0] # 해당 자리에 학생이 앉음

# 학생 만족도 구하기
student.sort() # 학생 번호 순으로 정렬
result = 0
for i in range(n):
	for j in range(n):
		like = 0
		for ii in range(4):
			nx = i + dx[ii]
			ny = j + dy[ii]
			if 0<=nx<n and 0<=ny<n:
				if board[nx][ny] in student[board[i][j]-1]:
					like += 1
		if like:
			result += 10**(like-1)
print(result)

