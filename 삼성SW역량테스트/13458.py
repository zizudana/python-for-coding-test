# 시험 감독
import sys

n = int(input()) # n개 시험장
a_list = list(map(int, sys.stdin.readline().split()))  # 응시자 수 배열
b, c = map(int, input().split())  # 총감독관 b명 감독, 부감독관 c명 감독 가능

cnt = n  # 각 시험장마다 총감독관 1명씩 배정
for i in range(n):
  num = a_list[i] - b  # 남은 응시자 수 num
  if (num > 0):
    cnt = cnt + num // c
    if (num % c):
      cnt = cnt + 1
print(cnt)