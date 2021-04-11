# 197p 부품 찾기
import sys
n = int(input())
array = list(map(int, sys.stdin.readline().split()))
array.sort()  # 이진 탐색을 위해 정렬
m = int(input())
x = list(map(int, sys.stdin.readline().split()))


# 이진 탐색(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in x:
    result = binary_search(array, i, 0, n-1)
    if result is not None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
