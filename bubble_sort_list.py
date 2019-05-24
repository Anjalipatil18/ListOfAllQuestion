#bubble sort 
l=[10,18,78,1,0]
i=0
while i<len(l):
	j=0
	while j<len(l):
		if l[i]<l[j]:
			temp=l[i]
			l[i]=l[j]
			l[j]=temp
		j=j+1
	i=i+1
print l