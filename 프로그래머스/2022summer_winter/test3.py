line = "64E2"
board = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']]
result = []
ltmp = [1, 0]
rtmp = [1, 9]
for a in line:
	flag = 0
	for ii in range(2):
		for jj in range(10):
			if a == board[ii][jj]:
				i = ii
				j = jj
				break
	ldis = abs(ltmp[0]-i) + abs(ltmp[1]-j)
	rdis = abs(rtmp[0]-i) + abs(rtmp[1]-j)
	if ldis > rdis:
		result.append(1)
		flag = 1
	elif ldis < rdis:
		result.append(0)
	else:
		if abs(ltmp[1]-j) < abs(rtmp[1]-j):
			result.append(0)
		elif abs(ltmp[1]-j) > abs(rtmp[1]-j):
			result.append(1)
			flag = 1
		else:
			if j<=4:
				result.append(0)
			else:
				result.append(1)
				flag = 1
	if flag:
		rtmp[0] = i
		rtmp[1] = j
	else:
		ltmp[0] = i
		ltmp[1] = j
	print(ltmp)
	print(rtmp)

for i in result:
	print(i)