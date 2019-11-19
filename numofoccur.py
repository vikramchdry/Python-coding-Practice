

'''def countoccurence(arr,n,x):
	count = 0
	for i in range(n):
		if arr[i]==x:
			count +=1
	return count






arr = [1, 2, 2, 2, 2, 3, 4, 7 ,8 ,8] 
n = len(arr) 
x = 2
print (countoccurence(arr, n, x)) 
'''


#------------>>>>>>>>>>>>Using binery Trees------------->>>>>>..

'''def binarySearch(arr,l,r,x):
	if (r<l):
		return -1
	mid = int(l+(r-l)/2)

	if arr[mid]==x:
		return mid

	if arr[mid] > x: 
        return binarySearch(arr, l,  
                            mid - 1, x) 
    return binarySearch(arr, mid + 1, 
                                r, x) 



def countoccurence(arr,n,x):'''


'''s = "vikram is a bad boy"
a = s.split()
st = []
for i in a:
	a = i[::-1]
	st.append(a)

output = ' '.join(st)

	#return output
print(output)'''


'''def findoccurence(arr,n,k):
	for i in range(n):
		for j in range(i+1):
			print(j)

		#print(i)
			#if arr[i]== arr[k]:
				#print(i)
		

arr= [1,2,3,4,4,5,6,6,6,7]
n = len(arr)
k = 4

findoccurence(arr,n,k) '''



































#-------------- find first occurence of kth element in an array---------------------------

def findfirst(arr,n,x):

	a = arr.sort();
	print(a)
x = 20; 
arr = [10, 30, 20, 50, 20]; 
n = len(arr)
findfirst(arr,n,x)



