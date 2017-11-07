# Uses python3
import sys

def get_fibonacci_huge_efficient(n):
    n=n%60
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum=1
    for i in range(n-1):
        previous,current=current,(current+previous)%10
        sum=(sum+current)%10
    return sum



    # n=n%PisonaNumebr
    # if n <=1:
    #     return n
    # previous =0
    # current =1
    # for i in range(n-1):
    #     previous,current=current,(previous+current)%m

    # return current


if __name__ == '__main__':
    # input=raw_input()
    # n=int(input)
    input = sys.stdin.read()
    # n, m = map(int, input.split())
    n=int(input)
    print(get_fibonacci_huge_efficient(n))
