'''def fib(n):
	#base case 
	if n ==0:
		return 0
	elif n ==1:
		return 1		
	return fib(n-1)+fib(n-2)


print(fib(25))'''


'''def fibbo(n):
	a =0
	b =1
	if n<0:
		print("Incorrect number")
	elif n == 0:
		return a
	elif n ==1:
		return b

	else:
		for i in range(2,n+1):'''




import random as r
import math as m

# Number of darts that land inside.
inside = 0
# Total number of darts to throw.
total = 1000

# Iterate for the number of darts.
for i in range(0, total):
  # Generate random x, y in [0, 1].
  x2 = r.random()**2
  y2 = r.random()**2
    # Increment if inside unit circle.
if m.sqrt(x2 + y2) < 1.0:
      inside += 1

# inside / total = pi / 4
pi = (float(inside) / total) * 4

# It works!
print(pi)
			