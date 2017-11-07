# Uses python3
import sys

def get_fibonacci_sum_last_efficient(n):
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



def fibonacci_partial_sum_naive(f,t):
    sum_f=get_fibonacci_sum_last_efficient(f-1)
    sum_t=get_fibonacci_sum_last_efficient(t)
    if (sum_t >= sum_f):
        return (sum_t-sum_f)
    else:
        return (10-sum_f+sum_t)





if __name__ == '__main__':
    input = sys.stdin.read();
    # input=raw_input()
    f,t = map(int, input.split())
    print(fibonacci_partial_sum_naive(f,t))