# https://programmers.co.kr/learn/courses/30/lessons/76502
op = ['(', '{', '[']
cl = [')', '}', ']']

def roll(s):
    s = s[1:] + s[0]
    return s


def isTrue(s):
    st = []
    flag = True
    for i in s:
        if i in op:
            st.append(i)
        else:
            if len(st) > 0 and op[cl.index(i)] == st[-1]:
                st.pop()
            else:
                flag = False
                break
    if flag and len(st) == 0:
        return True
    else:
        return False


def solution(s):
    answer = 0
    for _ in range(len(s)):
        if isTrue(s):
            answer += 1
        s = roll(s)
    return answer


s = "[](){}"
print(solution(s))
