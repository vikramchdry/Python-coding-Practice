'''def my_function(s):
	for ch in s:
		#print(ch)
		output = " "
		if ch.isalpha():
			output = output+ch
			#print(output)
			x = ch
			print(x)
		else:
			d = int(ch)
			newchar = chr((ord(x)+d))
			#print(newchar)
			#print(d)


my_function('a4k3b2')'''


'''def my_fun(s):
	for word in s:
		output = ""
		if word.isalpha():
			#output = output+word
			x = word
			#print(x)
		else:
			d = int(word)
			output = output+x*d
			print(output)
			

my_fun('a4k3b2')'''

class Test:
	def average(self,list):
		result = sum(list)/len(list)
		print(list)

t = Test()
t.average([10,20,30,40])



