rooms = ["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"]
target = 403
dic = {}
for room in rooms:
	room = room.lstrip('[')
	room = list(room.split(','))
	room[0] = list(room[0].split(']'))
	num = int(room[0][0])
	if num == target:
		continue
	if room[0][1] in dic.keys():
		dic[room[0][1]] += [num]
	else: 
		dic[room[0][1]] = [num]
	for i in range(1, len(room)):
		if room[i] in dic.keys():
			dic[room[i]] += [num]
		else:
			dic[room[i]] = [num]
dic = dict(sorted(dic.items()))
print(dic)

