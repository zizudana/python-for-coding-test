# 치킨 배달
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n*n 크기, 최대 m개 치킨집
# 빈칸 0 집 1 치킨집 2
board = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []
for i in range(n):
  for j in range(n):
    if board[i][j] == 1: # 집이면
      house.append([i, j])
    elif board[i][j] == 2: # 치킨집이면
      chicken.append([i, j])
m_chicken = list(combinations(chicken, m)) # m개 치킨집 조합

min_sum = 1e9
for ch in m_chicken:
  dis_sum = 0
  for h in house:
    min_dis = 3*n
    for i in range(m):
      dis = abs(h[0]-ch[i][0]) + abs(h[1]-ch[i][1]) # 한 집의 치킨거리
      min_dis = min(min_dis, dis) 
    dis_sum += min_dis # 총 치킨거리에 더해준다
  min_sum = min(min_sum, dis_sum)

print(min_sum)
