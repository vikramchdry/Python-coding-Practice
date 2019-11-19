'''def squaroot(x):
	if(x==0 or x == 1):
		return x
	i = 1
	result = 1
	while (result<=x):
		i +=1
		print(i)
		result= i*i
		print("<<<<<<<<<--------------->>>>>")
		print(result)
	return i-1

x = 11
print(squaroot(x))'''



'''def findoccurrence(arr,k,n):
	for i in range(0,n):
		if(arr[i]==k):
			print(i) 

arr = [1,2,3,4,5,6,7,8]
k = 5
n = len(arr)
print(findoccurrence(arr,k,n))'''


'''def binerysearch(arr,l,e,x):

	#base case of an problem
	if e>=l:
		mid = l +(r-1)/2

	#element is mid number itself
	if arr[mid]==x:
		return mid
	elif arr[mid]>x:
		return binerysearch(arr,l,mid-1,x)
	elif arr[mid]<x:
		return binerysearch(arr,mid+1,r,x)
	else:
		return -1


arr = [ 2, 3, 4, 10, 40 ]
x=4
r= len(arr)-1
result = binerysearch(arr,0,r,x)
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")'''


# Python Program for recursive binary search. 

# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 

	# Check base case 
	if r >= l: 

		mid = l + (r - 1)//2

		# If element is present at the middle itself 
		if arr[mid] == x: 
			return mid 
		
		# If element is smaller than mid, then it 
		# can only be present in left subarray 
		elif arr[mid] > x: 
			return binarySearch(arr, l, mid-1, x) 

		# Else the element can only be present 
		# in right subarray 
		else: 
			return binarySearch(arr, mid + 1, r, x) 

	else: 
		# Element is not present in the array 
		return -1

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10

# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 

if result != -1: 
	print("Element is present at index % d" % result )
else: 
	print("Element is not present in array")





