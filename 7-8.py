# 201p 떡볶이 떡 만들기 (파라메트릭 서치 문제 - 이진 탐색을 반복문으로 구현)
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid  # 잘린 떡 길이를 total에 더하기
    if total < m:  # 총 합이 더 작으면
        end = mid - 1  # 더 많이 자름
    else:  # 총 합이 더 크면
        result = mid  # result에 저장해 두고
        start = mid + 1  # 더 조금 자름

print(result)
