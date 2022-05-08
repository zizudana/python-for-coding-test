# https://programmers.co.kr/learn/courses/30/lessons/17686
files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

def solution(files):
	answer = []
	file_dic = {}
	for i in range(len(files)):
		file_dic[i] = list(files[i])
	for name in list(file_dic.values()):
		for c in name:
			if c.isalpha():
				c = c.lower()
			else:
				break
	file_dic = dict(sorted(file_dic.items(), key=lambda x: x[1]))
	for n in range(len(file_dic)):
		temp = ""
		for i in range(len(file_dic[n])):
			if file_dic[n][i].isdigit():
				while file_dic[n][i].isdigit():
					temp += file_dic[n][i]
					i += 1
				break
		file_dic[n] = int(temp)
	file_dic = dict(sorted(file_dic.items(), key=lambda x: x[1]))
	for i in list(file_dic.keys()):
		answer.append(files[i])
	return answer

print(solution(files))