def first_recurring(s):
	counts = {} # dictionary or hash table
	for char in s:
		if char in counts:
			return char
		print(counts)
		counts[char] = 1
	return None

s = "horizon tutorials"
print(first_recurring(s))