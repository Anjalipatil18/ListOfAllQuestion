# sub_string="abcdefghiabczabcfabca"
# print sub_string[0:4]
# print sub_string[4:8]
# print sub_string[8:12]
# print sub_string[12:16]
# print sub_string[16:20]
# print sub_string[20:21]


sub_string="abcdefghijklmnop0uhjhjh"
string="abcd"
i=0
l=len(string)
while i<len(sub_string):
	j =  sub_string[i:i+l]
	print j
	i=i+l	