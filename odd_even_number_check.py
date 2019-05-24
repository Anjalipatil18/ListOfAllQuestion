element=[23,14,56,12,19,9,15,25,31,42,43]
num1=0
while num1<len(element):
	if element[num1]%2==0:
		print "its evan no.", str(element[num1])
		print " "
	else:
		print "its odd no." , str(element[num1])
	num1=num1+1