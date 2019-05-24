binary_number=[1,0,0,1,1,0,1,1]
sum=0
b=1/2
i=(len(binary_number)-1)
while i>=0:
	c= binary_number[i]*(2**(b))
	print c
	sum=sum+c
	b=b+1
	i=i-1
print "all decimal no sum=",sum

