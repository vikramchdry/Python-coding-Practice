
'''def my_function(s):
	str = ''
	for i in s:
		str = i+str
	print(str)
'''
def my_function(s):
	s = s.split()
	#print(s)
	lst = []
	for i in s:
		lst.append(i[::-1])
		newlst = ' '.join(lst)
	#print(lst)
	return newlst

s = "Learning python is very easy"
print(my_function(s))