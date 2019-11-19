'''s = "B4A1D3"
alphabets = []
digits = []

for ch in s:
	if ch.isalpha():
		alphabets.append(ch)

	else:
		digits.append(ch)
print(alphabets)
print(digits)

output = ''.join(sorted(alphabets)+sorted(digits))
print(output)'''

#2. write a program for the following requiement.

'''s = "a4b3c2"
output = ''
for ch in s:
	if ch.isalpha():
		x = ch
	else:
		d = int(ch)
		output = output + x*d
print(output)'''

#fruits = ["apple", "banana", "cherry"]
for x in range(6):
	print(x)