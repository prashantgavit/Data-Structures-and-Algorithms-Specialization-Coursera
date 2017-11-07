# Uses python3

n = int(input())
a=[int(x) for x in input().split(' ')]
assert(len(a) == n)
max1_index=-1
max2_index=-1
for i in range(0, n):
	if (max1_index==-1 or a[i]>a[max1_index] ):
		max1_index=i

for i in range(0,n):
	if ((max2_index==-1 or a[i]>a[max2_index]) and i!=max1_index):
		max2_index=i	

print(a[max1_index]*a[max2_index])
