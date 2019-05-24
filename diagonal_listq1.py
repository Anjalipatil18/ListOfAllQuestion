a=[[8,3,4],[1,5,9],[6,7,2]]
i=0
new_list=[]
sum=0
j=0
while i<(len(a)):
	new_list.append(a[-i][-j])
	sum=sum+new_list[i]
	i=i+1
print new_list
print sum