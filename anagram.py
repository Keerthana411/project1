str1=input("enter the string1")
str2=input("enter the string2")
str1=str1.lower()
str2=str2.lower()
if (len(str1)) == (len(str2)):
	x=sorted(str1)
	y=sorted(str2)
	if (x) == (y):
		print( str1 + " and " + str1 + " are anagram " )
	else:
		print(str1+ " and " +str2+" are not anagram ")
else:
	print(str1+ " and " +str2+" are not anagram ")
