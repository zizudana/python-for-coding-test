# https://programmers.co.kr/learn/courses/30/lessons/76501 음양더하기

def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer