mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
new=mainStr.split(" ")
print new
subStr = "over"
replacementStr = "on"
i=0
new_list=[]
while i<len(new):
	if new[i] == subStr:
		new[i] = replacementStr
	i=i+1
print new

