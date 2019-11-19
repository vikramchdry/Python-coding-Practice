#1. Question:-Python program to print even length words in a string ------>>>>>>

'''def length_of_even_word(s):   # method for our code
	l=s.split()                 # we need to split sentence into lsit and store this list into the new variable l
	#print(l)
	

	for word in l:                        # for loop to itrate values of list becuase we need to print out even words 
		if len(word)%2==0:
			print(word)



#s = "This is a python language"
s = "i am muskan"
length_of_even_word(s)'''



#2.write a program to print out even index of given string

#Method 1 using while loop

'''def even_index(s):

	i = 0
	print("The character present at even index")
	while i<len(s):
		print(s[i])
		i = i+2

	i = 1
	print("The character present at odd index")
	while i<len(s):
		print(s[i])
		i = i+2

s = "VikramSingh"
even_index(s)'''

def evenoddindex(s):

	print("The character present at even index")
	s = s[0::2]
	print(s)
	print("The character present at odd index")
s = "vikram"
evenoddindex(s)