sub_string="abcdefghiabczabcfabc"
new_list=""
substr="abc"
i=0
while i<len(sub_string):
	if sub_string[i] not in substr:
		new_list = new_list+sub_string[i]
	i=i+1
print new_list


