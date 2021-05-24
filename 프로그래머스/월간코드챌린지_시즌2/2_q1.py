"""
def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            n1 = str(format(num, 'b'))
            n2 = num
            while True:
                over_flag = False
                n2 += 1
                sn2 = str(format(n2, 'b'))
                if len(n1) < len(sn2):
                    n1 = '0'+n1
                count = 0
                for i in range(len(n1)):
                    if n1[i] != sn2[i]:
                        count += 1
                        if count > 2:
                            over_flag = True
                            break
                if not over_flag:
                    break
            answer.append(n2)

    return answer

numbers = [2, 7]
print(solution(numbers))
"""
def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            n1 = str(format(num, 'b'))
            n1 = '0' + n1
            n1 = list(n1)
            for i in range(len(n1)-1, -1, -1):
                if n1[i] == '0':
                    n1[i] = '1'
                    n1[i+1] = '0'
                    break
            n2 = "".join(n1)
            n2 = int(n2, 2)
            answer.append(n2)
    return answer
numbers = [2, 7]
print(solution(numbers))
