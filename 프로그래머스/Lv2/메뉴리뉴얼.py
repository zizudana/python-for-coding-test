from itertools import combinations
from collections import Counter
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

def solution(orders, course):
	answer = []
	for c in course:
		tmp = []
		for order in orders: # c개의 조합을 구함
			tmp += combinations(sorted(order), c)
		cnt = Counter(tmp) #각 조합의 개수
		if len(cnt) > 0:
			max_cnt = max(cnt.values())
			if max_cnt >= 2:
				for k, v in cnt.items():
					if v == max_cnt:
						answer.append(''.join(k))
	return sorted(answer)

print(solution(orders, course))