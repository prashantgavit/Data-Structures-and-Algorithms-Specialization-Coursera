# use python3
n=int(input())
temp1=0
temp2=1
temp3=2
if n==0:
	Fb=0

if n==1:
	Fb=1

if n>=2:
	for i in range(2,n+1):
		temp3=temp1+temp2
		temp1=temp2
		temp2=temp3
	Fb=temp2

print(Fb)

		
	
