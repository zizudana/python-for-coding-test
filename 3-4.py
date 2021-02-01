N, K = map(int, input().split())
N2, K2 = N, K
count = 0

while N != 1:
  count += 1
  if N % K == 0:
    N /= K 
  else:
    N -= 1

print(count)

count2 = 0
#N이 K의 배수가 되도록 한번에 빼기
while True:
  # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
  target = (N2 // K2) * K2
  count2 += (N2 - target)
  N2 = target 
  # N이 K보다 작을 때 반복문 탈출
  if N2 < K2:
    break
  # N을 K로 나누기
  count2 += 1
  N2 //= K2

# 마지막으로 남은 수에 대하여 1씩 빼기
count2 += (N2 - 1)
print(count2)