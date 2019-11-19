
def linearsearch(arr,n ,x):
	for i in range(0,n):
		if(arr[i]==x):
			return True
		return False

def findpair(arr,n,x):

	for i in range(0,n-1):
		if (linearsearch((arr+i+1),n-i-1,x-arr[x])):
			return True
		return False

arr = [2,9,7,4,5,1,0,8]
n = len(arr)
x = 18
findpair(arr,n,x)
