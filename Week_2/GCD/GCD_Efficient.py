# This is also known as Eclud GCD
[a,b]=[int(x) for x in input().split(' ')]

def Fun_GCD(a,b):
	if (b==0):
		return(a)
	
	else:
		a_prime=a%b
		return(Fun_GCD(b,a_prime))


print(Fun_GCD(a,b))

