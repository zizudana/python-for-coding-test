atmos = [[80, 35], [70, 38], [100, 41], [75,30], [160,80], [77, 29], [181, 68], [151, 76]]

cnt = 0
day = 0
flag = 0 # 마스크를 썼는지
for a in atmos:
	if a[0]>=151 and a[1]>=76: # 둘 다 매우나쁨
		if not flag:
			cnt+=1
			print(a)
		flag = 0
		continue
	if a[0]>=81 or a[1]>=36:
		if not flag:
			cnt += 1 # 마스크 첫사용
			day = 0
			print(a)
			flag = 1
	if flag:
		day += 1
		if day > 2:
			flag = 0 # 마스크 폐기
print(cnt)