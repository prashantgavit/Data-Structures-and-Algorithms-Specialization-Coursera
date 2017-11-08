# Uses python3
import sys

def get_change(m):
    coinList=[10,5,1]
    numCoin=0
    remainingCoin=m
    for coin in coinList:
        numCoin=numCoin+(remainingCoin//coin)
        remainingCoin=remainingCoin%coin
    #write your code here
    return numCoin

if __name__ == '__main__':
    m = int(sys.stdin.read())
    r=int(m)
    print(get_change(r))
