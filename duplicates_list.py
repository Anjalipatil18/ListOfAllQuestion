# n = [19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
# new_list=[]
# i=0
# while i<len(n):
# 	j=0
# 	while j<len(n):
# 		if n[i] not in new_list:
# 			if n[i]==n[j]:
# 				new_list.append(n[i])
# 			j=j+1
# 		i=i+1
# print new_list

# new=[]
# new_list=[]
# i=0
# while i<len(n):
# 	if n[i] not in new_list:
# 		n.remove(n[i])
# 		if new_list[i] in n:
# 			new.append(new_list[i])
# 		else:
# 			i=i+1
# 	i=i+1
# print new

n = [19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
new_list=[]
i=0
count=0
while i<len(n):
    j=i+1
    while j<len(n):
        if n[i]==n[j]:
            count=count+1
            if count >= 1:
                if n[i] not in new_list:
                    new_list.append(n[i])
        j=j+1
    i=i+1
print new_list