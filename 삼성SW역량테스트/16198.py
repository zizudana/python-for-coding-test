# 에너지 모으기
n = int(input()) # 에너지 구슬의 개수
weight = list(map(int, input().split())) # 에너지 구슬의 무게

def recur(w):
	if len(w) == 3: # 길이가 3이 되면 return
		return w[0] * w[2]
	max_result = 0
	for i in range(1, len(w)-1):
		result = w[i-1] * w[i+1] + recur(w[:i] + w[i+1:])
		max_result = max(result, max_result)
	return max_result

print(recur(weight))
		