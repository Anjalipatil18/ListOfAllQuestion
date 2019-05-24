char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
new_list=[]
i=0
while i<len(char_list):
	j=0
	count=0
	while j<len(char_list):
		if char_list[i] == char_list[j]:
			count=count+1
		j=j+1
	if [char_list[i],count] not in new_list:
		new_list.append([char_list[i],count])
			
	i=i+1
print new_list
