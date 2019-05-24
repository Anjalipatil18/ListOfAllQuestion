i=1
j=2
while i>=1:
	a=""*j+"1"*i+""*j
	print a
	i=i+2
	j=j-1
	if i>5:
		break
i=3
j=1
while i>=1:
	a=""*j+"1"*i+""*j
	print a
	i=i-2
	j=j+1


i = 1
j = 2
while i>=1:
  print  " "*j+"1"*i+" "*j
  i = i+2
  j = j-1
  if i>5:
    break
i = 3
j = 1
while i>=1:
  print  " "*j+"1"*i+" "*j
  i = i-2
  j = j+1

list1=[[1,2,3],[4,5,6],[7,8,9]]
i=0
count=0
while i<len(list1):
	j=0
	sum=0
	while j<len(list1[i]):
		sum=sum+list1[i][j]
		j=j+1
	count=(count+sum)
	i=i+1
print "count=",count
count="45"
print list(count)
int_count=int(count)
print int(count[0])+int(count[1])
if int_count==1:
	print "kalinga number hai"
else:
	print "kalinga number nahi hai"
