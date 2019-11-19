
'''def pairsumofgiven(arr,n,sum):
	#lower index
	l = 0
	#higher index
	h = n-1
	while (l<h):
		if (arr[l]+arr[h]>sum):
			h -= 1
		elif (arr[l]+arr[h]<sum):
			l += 1
		elif (arr[l]+arr[h]==sum):
			pair =  (l,h)
			print(pair)
			break


a = [10, 20, 30, 40,45,5, 50]
sum = 50
n = len(a)
pairsumofgiven(a,n,sum)'''

def printpair(arr,n,sum):
	for i in range(0,n):
		for j in range(i+1,n):
			print(j)
			'''if (arr[i]+arr[j] ==sum):
				print("(", arr[i],  
                      ", ", arr[j],  
                      ")", sep = "")'''




arr = [1, 5, 7, -1, 5] 
n = len(arr) 
sum = 6
printpair(arr, n, sum) 



