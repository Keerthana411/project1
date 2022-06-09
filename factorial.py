def factorial(k):
	if (k == 1):
		return k
	else:
		return k*factorial(k-1)
k=int(input("enter a number"))
f=factorial(k)
print("the factorial of k is ",f)
