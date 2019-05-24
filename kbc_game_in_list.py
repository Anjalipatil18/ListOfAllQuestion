question_list = [
	"1. How many continents are there?",  			# pehla question
	"2. What is the capital of India?",			# doosra question
	"3. NG mei kaun se course padhaya jaata hai?"	# teesra question
]

options_list = [
	#pehle question ke liye options
	["(1) Four","(2) Nine","(3) Seven","(4)Eight"],
	#second question ke liye options
	["(1)Chandigarh","(2) Bhopal","(3) Chennai","(4) Delhi"],
	#third question ke liye options
	["(1) Software Engineering", "(2) Counseling", "(3) Tourism", "(4) Agriculture"]
]
life_line = [["(2) Nine","(3) Seven"],["(3) chennai, (4)Delhi"],["(1)Software Engineering,(2)Counseling"]]
# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1]
i=0
while i<len(question_list):
	print question_list[i]
	print options_list[i]
	user_input=input("enter the life_line=")
	if 5050==user_input:
		print question_list[i]
		print life_line[i]
		user_input=input("enter your answer")
	if solution_list[i]==user_input:
		print "your answer is right"
		print "***********************************************************************************"
	else:
		print "your answer is wrong"
		print "************************************************************************************"
	i=i+1
	
