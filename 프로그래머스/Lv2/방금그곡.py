# https://programmers.co.kr/learn/courses/30/lessons/17683 방금그곡
m = "ABCDEFG"
m2 = "CC#BCC#BCC#BCC#B"
m3 = "ABC"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
musicinfos2 = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
musicinfos3 = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]

# C C# D D# E F F# G G# A A# B
# C c D d E F f G g A a B
def new_music(music): # 소문자로 바꾸기
	tmp = ""
	i = 0
	while i+1 < len(music):
		if music[i+1] == "#":
			tmp += music[i].lower()
			i += 1
		else:
			tmp += music[i]
		i += 1
	if i == len(music)-1:
		tmp += music[i]
	return tmp

# 음악시작시간, 끝난시간, 제목, 악보정보
def solution(m, musicinfos):
	answer = []
	m = new_music(m)
	for musicinfo in musicinfos:
		musicinfo = list(musicinfo.split(','))

		# 재생시간 계산 (musiclen)
		musicinfo[0] = list(map(int, musicinfo[0].split(':'))) # 시작시간
		musicinfo[1] = list(map(int, musicinfo[1].split(':'))) # 끝난시간
		musiclen = (musicinfo[1][0] * 60 + musicinfo[1][1]) - (musicinfo[0][0] * 60 + musicinfo[0][1])

		# 실제 재생된 음악 구하기
		music = new_music(musicinfo[3])
		tmp = ""
		tmp += music * (musiclen // len(music))
		tmp += music[:musiclen % len(music)]

		# 멜로디가 있는지 확인
		if m in tmp:
			answer.append((musicinfo[2], musiclen)) # (음악제목, 재생시간)

	if not answer:
		return "(None)"
	if len(answer) > 1:
		answer.sort(key=lambda x:-x[1]) # 재생시간이 긴 순으로 정렬
	return answer[0][0]

print(solution(m, musicinfos))