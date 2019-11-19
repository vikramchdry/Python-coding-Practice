

def printPairs(arr, n, sum):

	hs = set()
	for i in range(0,n):
		temp = sum -arr[i]
		if temp in hs:
			print("pair with given sum" +" " + str(sum) +" "+ "is "+ str(arr[i])+ ", "+ str(temp))
		hs.add(arr[i])







arr = [1, 4, 45, 6, 10, 8] 
n =len(arr)
sum = 14
printPairs(arr,n,sum)