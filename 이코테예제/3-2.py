#N, M, K를 공백으로 구분하여 입력받기
N, M, K = map(int, input().split())
#N개의 수를 공백으로 구분하여 입력받기
num_list = list(map(int, input().split()))

num_list.sort(reverse = True) #입력받은 수들 정렬하기
result = 0
count = 0

while True:
  for i in range(K): #가장 큰 수를 K번 더하기
    result += num_list[0] #가장 큰 수
    count += 1 #더할 때마다 1씩 더하기
    if count >= M:
      break
  result += num_list[1] #두 번째로 큰 수
  count += 1 #더할 때마다 1씩 더하기
  if count >= M:
      break
    
print(result)

#수열을 이용해서 풀기
first_count = M // (K+1) 
second_count = first_count # 두 번째로 큰 수가 더해지는 횟수
first_count *= K
first_count += M % (K+1) #가장 큰 수가 더해지는 횟수
result2 = num_list[0] * first_count + num_list[1] * second_count
print(result2)