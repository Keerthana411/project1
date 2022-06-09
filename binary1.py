#binary search
def binarysearch(a,l,h,b):
	if h>=l:
		m=(l+h)//2
		if a[m]==b:
			return a[m]
		elif a[m]>b:
			return binarysearch(a,l,m-1,b)
		else:
			return binarysearch(a,m+1,h,b)
	else:
		return -1
a=[1,2,3,4,5,6,7,8,9]
b=int(input("enter the element to search"))
result=binarysearch(a,0,len(a)-1,b)
if result!=-1:
	print("element is present")
else:
	print("element is not present")
