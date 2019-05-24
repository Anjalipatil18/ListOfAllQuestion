marks=[[78,76,94,86,88],[91,71,98,65],[95,45,78]]
i=0
b=1
while i<len(marks):
	j=0
	count=0
	while j<len(marks[i]):
		count=count+marks[i][j]
		average=count/len(marks[i])
		j=j+1
	print count
	print b, "year ka average:",average
	i=i+1
	b=b+1