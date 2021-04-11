num=input()
count = 0

while num[count]=='0':
  count += 1

result = int(num[count])

for i in range(count+1, len(num)):
  if int(num[i]) < 2:
    result += int(num[i])
  else:
    result *= int(num[i])

print(result)