# 큐빙
t = int(input()) # 테스트케이스 t개

def turn(cube, face): # 면 내부에서 시계방향 회전
	temp = cube[face][0][0]
	cube[face][0][0] = cube[face][2][0]
	cube[face][2][0] = cube[face][2][2]
	cube[face][2][2] = cube[face][0][2]
	cube[face][0][2] = temp
	temp = cube[face][0][1]
	cube[face][0][1] = cube[face][1][0]
	cube[face][1][0] = cube[face][2][1]
	cube[face][2][1] = cube[face][1][2]
	cube[face][1][2] = temp

def move(cube, face):
	if face == 'U': # 윗면
		temp = cube[0][0]
		cube[0][0] = cube[4][0]
		cube[4][0] = cube[5][0]
		cube[5][0] = cube[3][0]
		cube[3][0] = temp
		turn(cube, 2) # 윗 면을 돌려준다
	elif face == 'D': # 아랫면
		temp = cube[0][2]
		cube[0][2] = cube[3][2]
		cube[3][2] = cube[5][2]
		cube[5][2] = cube[4][2]
		cube[4][2] = temp
		turn(cube, 1) 
	elif face == 'F': # 앞면
		temp = cube[2][2]
		cube[2][2] = [cube[3][2][2], cube[3][1][2], cube[3][0][2]]
		cube[3][0][2], cube[3][1][2], cube[3][2][2] = cube[1][0]
		cube[1][0] = [cube[4][2][0], cube[4][1][0], cube[4][0][0]]
		cube[4][0][0], cube[4][1][0], cube[4][2][0] = temp
		turn(cube, 0)
	elif face == 'B': # 뒷면
		temp = cube[2][0]
		cube[2][0] = [cube[4][0][2], cube[4][1][2], cube[4][2][2]] 
		cube[4][2][2], cube[4][1][2], cube[4][0][2] = cube[1][2]
		cube[1][2] = [cube[3][0][0], cube[3][1][0], cube[3][2][0]]
		cube[3][2][0], cube[3][1][0], cube[3][0][0] = temp
		turn(cube, 5)
	elif face == 'L': # 왼쪽면
		temp = [cube[0][0][0], cube[0][1][0], cube[0][2][0]]
		cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
		cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[5][2][2], cube[5][1][2], cube[5][0][2]
		cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[1][2][0], cube[1][1][0], cube[1][0][0]
		cube[1][0][0], cube[1][1][0], cube[1][2][0] = temp
		turn(cube, 3)
	
	elif face == 'R': # 오른쪽면
		temp = [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
		cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
		cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
		cube[5][0][0], cube[5][1][0], cube[5][2][0] = cube[2][2][2], cube[2][1][2], cube[2][0][2]
		cube[2][0][2], cube[2][1][2], cube[2][2][2] = temp
		turn(cube,4)

for _ in range(t):
	n = int(input()) # 큐브를 돌린 횟수
	arr = list(map(str, input().split())) # 큐브를 돌린 방법 (돌린면돌린방향)
	cube = [[] for _ in range(6)] 
	# 앞면 밑면 윗면 왼쪽 오른쪽 뒷면
	for _ in range(3): # 초기화
		cube[0].append(['r', 'r', 'r'])
		cube[1].append(['y', 'y', 'y'])
		cube[2].append(['w', 'w', 'w'])
		cube[3].append(['g', 'g', 'g'])
		cube[4].append(['b', 'b', 'b'])
		cube[5].append(['o', 'o', 'o'])
	for ar in arr:
		face, di = ar
		if di == '+':
			cnt = 1
		else:
			cnt = 3
		for _ in range(cnt):
			move(cube, face)
	for i in range(3):
		for j in range(3):
			print(cube[2][i][j], end="")
		print()
