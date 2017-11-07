# Uses python3
import sys

def gcd_efficient(a, b):
	if (a % b == 0):
		return(b)
	else:
		return(gcd_efficient(b,a%b))

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split(" "))
    print(gcd_efficient(a, b))
