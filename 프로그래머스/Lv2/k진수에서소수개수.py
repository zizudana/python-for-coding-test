import math
n = 110011
k = 10

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    result = 0
    conv = ""
    if k == 10:
        n_list = str(n).split('0')
        for i in n_list:
            if i and is_prime(int(i)):
                result += 1
        return result
    while (n > 0):
        conv += str(n % k)
        n = n // k
    conv = conv[::-1]
    conv_list = conv.split('0')
    for c in conv_list:
        if c and is_prime(int(c, 10)):
            result += 1
    return result

print(solution(n, k))