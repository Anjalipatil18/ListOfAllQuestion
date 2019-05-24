s = "shrivas"
length = len(s)
i = 0
while i < length / 2 + 1:
    if s[i] != s[-i - 1]:
        print "not Palindrome"
        break
    i =i + 1
else:
    print " Palidrome"