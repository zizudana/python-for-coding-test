# N, M을 공백으로 구분하여 입력받기
N, M = map(int, input().split())

min_list = []
# 한 줄씩 입력받아 확인
for n in range(N):
  num_list = list(map(int, input().split()))
  # 현재 줄에서 가장 작은 수 찾기
  min_list.append(min(num_list))
print(max(min_list)) # 가장 작은 수 중에서 가장 큰 수 찾기