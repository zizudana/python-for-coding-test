s = "aabbaccc"

def solution(s):
    slen = len(s) # 문자열 길이 slen
    answer_list = []
    if slen == 1:
        return 1
    for tlen in range(1, slen//2 + 1): # tlen만큼 나눈다
        result = ""
        tmp = s[:tlen]
        cnt = 1
        for i in range(tlen, slen+tlen, tlen):
            if tmp == s[i:i+tlen]:
                cnt += 1
            else:
                if cnt == 1:
                    result += tmp
                else:
                    result += str(cnt) + tmp
                tmp = s[i:i+tlen]
                cnt = 1
        answer_list.append(len(result))
    answer = min(answer_list)
    return answer

solution(s)