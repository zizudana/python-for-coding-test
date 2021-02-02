n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

result = 0 # 총 그룹의 수
while len(num_list) > 0:
  i = num_list.pop(0)
  if i <= len(num_list):
    for j in range(i):
      num_list.pop(0)
    result += 1
  else: 
    break
print(result)
