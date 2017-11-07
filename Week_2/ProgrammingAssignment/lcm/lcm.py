#Uses python3
import sys

def gcm_efficient(a, b):
	if (a%b == 0):
		return(b)
	else:
		return (gcm_efficient(b,a%b))

def lcm_efficient(a,b):
	gcm=gcm_efficient(a,b)
	return(a*b//gcm)

if __name__ == '__main__':
	input = sys.stdin.read()
	a, b = map(int, input.split(" "))
	print(lcm_efficient(a, b))

