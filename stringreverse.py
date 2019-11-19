 #  Question1 --->>>>>>> Write a function to reverse string ........>>>>>>>>

""" Method 1 to reverse the given string using slicing

Slicing is nothing but it is to retrive the data in given data whatever it is?

Slicing operation:
 s[begin:end:step]
step means how much character it is skip while retrieving data

"""

"""def revstring(s):
	str = s[::-1]
	return str
print(revstring('Vikram'))"""


#Method 2 using For loop

"""def revstr(s):
	str = ""
	for i in s:
		str = i + str
		#print(str)
		
	return str
s = "string"
print(revstr(s))
"""


"""def my_function(s):
	return s[::-1]

string = my_function("I wonder how this text looks like backwards")
print(string)"""





# Using while loop character by character



'''def revstr(s):
	str = ''
	i = len(s)-1
	while i >= 0:
		str = str+s[i]
		i-1
		
s= "vikram"
print(revstr(s))'''






#2. Question:- write a Program to reverse order of words


'''def reverseword(s):
	l = s.split()
	revstr = l[::-1]
	string = ' '.join(revstr)
	return string	

s = "Learning python is very easy "
print(reverseword(s))'''



#3. Write a program to reverse internal content of each word


'''def revcontent(s):      # function to write reverse order of each words in sentenced
	l = s.split()    # split the given sentenced into the list
	lst = []         # new list variable to store words after running for loop(push the data into the list)
	print(l)
	for word in l:
		lst.append(word[::-1])
		revword = ' '.join(lst)
	print(lst)
	return revword
	
	
s = "Wroclaw University of science and Technology"
print(revcontent(s))'''





#4 Question ------->>>> Write a program to reverse internal content of every second word------->>



def rev_second_word(s):
	l = s.split()
	i = 0
	lst = []
	while i<len(l):
		if i%2 == 0:
			lst.append(l[i])
		else:
			lst.append(l[i][::-1])
		i = i+1
	lst = ' '.join(lst)
	print(lst)

s = "one two three four five six seven"
print(rev_second_word(s))


	
