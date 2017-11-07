
[a,b]=[int(x) for x in input().split(' ')]
def Fun_Min_Number(a,b):
	if (a>b):
		return(b)
	else:
		return(a)


def Fun_GCD(a,b):
	best=0
	n=Fun_Min_Number(a,b)
	for i in range(1,n+1):
		if (a%i==0 and b%i==0):
			best=i
	return(best)


print(Fun_GCD(a,b))
