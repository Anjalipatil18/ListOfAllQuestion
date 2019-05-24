numbers=[50,40,23,70,56,12,5,10,7]
i=0
maximum=numbers[i]
while i<len(numbers):
	if numbers[i]>maximum:
		maximum=numbers[i]
	i=i+1
y=0
second_maximum=0
while y<len(numbers):
	if maximum>numbers[y] and second_maximum<numbers[y]:
		second_maximum=numbers[y]
	y=y+1
print second_maximum
print maximum