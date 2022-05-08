fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
import math

result = []
dic = {}
for record in records:
	record = list(record.split())
	h, m = map(int, record[0].split(':'))
	if record[1] in dic.keys():
		dic[record[1]] += [h*60 + m]
	else:
		dic[record[1]] = [h*60+m]
dic=dict(sorted(dic.items()))

for value in dic.values():
	if len(value) % 2 != 0:
		value += [23*60+59]
	fee = 0
	t = 0
	for i in range(0, len(value)-1, 2):
		t += (value[i+1] - value[i])
	print(t)
	if  t <= fees[0]: # 기본시간 이하
		fee += fees[1]
	else:
		fee += fees[1]
		fee += (math.ceil((t-fees[0])/fees[2])*fees[3])
	result.append(fee)

print(result)