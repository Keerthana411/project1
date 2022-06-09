def c(p,r,t):
	if t==0:
		return p
	else:
		return c(p+(p*r)/100,r,t-1)
p=float(input("enter the principal amount"))
r=float(input("enter the rate of interest"))
t=float(input("enter the number of years"))
#ci=CompoundInterest(p,r,t)
print(c(p,r,t))

