# Uses python3
import sys

def get_fibonacci_huge_efficient(n, m):
    if n <= 1:
        return n
    PisonaNumebr=1
    previous = 0
    current  = 1
    while ([current,previous]!=[0,1]):
        previous,current=current,(current+previous)%m
        PisonaNumebr=PisonaNumebr+1

    n=n%PisonaNumebr
    if n <= 1:
        return n
    previous=0
    current=1
    for i in range(n-1):
        previous,current=current,(current+previous)%m
    return current



    # n=n%PisonaNumebr
    # if n <=1:
    #     return n
    # previous =0
    # current =1
    # for i in range(n-1):
    #     previous,current=current,(previous+current)%m

    # return current


if __name__ == '__main__':
    input=raw_input()
    input = sys.stdin.read()
    # n, m = map(int, input.split())
    print(get_fibonacci_huge_efficient(n, m))
