elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
even_no=0
odd_no=0
sum=0
sum1=0
i=0
while i<len(elements):
	if elements[i]%2==0:
		print elements[i]
		sum=sum+elements[i]
		even_no=even_no+1
		average_of_even_no=sum/even_no
	else:
		print elements[i]
		sum1=sum1+elements[i]
		odd_no=odd_no+1
		average_of_odd_no=sum1/odd_no
	i=i+1
print "even_no=",even_no
print "sum_of_even_no=",sum
print "average_of_even_no=",average_of_even_no
print "odd_no=",odd_no
print "sum_of_odd_no=",sum1
print "average_of_odd_no=",average_of_odd_no
