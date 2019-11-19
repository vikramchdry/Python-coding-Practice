# find out intersection of given array

#Naive approach 

def printIntersection(ar1,ar2,m,n):
	if m>n:
		temp = ar1      #we are make sure this things  ar[0---------m-1] shouls be smaller one array
		ar1 = ar2
		ar2 = temp

		temp1  = m
		m = n
		n = temp1


	ar1.sort()

	for i in range(0,n):
		if binarysearch(ar1,0,m-1,ar2[i] != -1):
			print(ar2[i], end = " ")


def binarysearch(ar,start,end,x):
	if (end>=1):
		mid = int(start +(start-end)/2)
		if ar[mid] == x:

			return mid
		if ar[mid]>x:
			return binarysearch(ar,start,mid-1,x)
		return binarysearch(ar,mid+1, end,x)
	return -1

	






ar1 = [7, 1, 5, 2, 3, 6]; 
ar2 = [3, 8, 6, 20, 7]; 
m = len(ar1); 
n = len(ar2); 
#print("\nIntersection of two arrays is "); 
printIntersection(ar1, ar2, m, n)