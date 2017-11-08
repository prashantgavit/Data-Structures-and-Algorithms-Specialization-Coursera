# Uses python3
import sys
def max_value_index(A):
    maxValue=A[0]
    index=0
    for i in range(len(A)-1):
        if A[i+1]>maxValue:
            maxValue=A[i+1]
            index=i+1
    return (index)

def get_optimal_value(capacity, weights, values):
    value = 0.
    unitValues=[]
    remainingCapacity=capacity
    for i in range(len(weights)):
        unitValues.append((values[i]/float(weights[i])))
    while (remainingCapacity>0) and (len(unitValues)!=0):
        maxIndex=max_value_index(unitValues)
        weightIndex=weights[maxIndex]
        unitIndex=unitValues[maxIndex]
        take=min(remainingCapacity,weightIndex)
        value=value+take*unitIndex
        remainingCapacity=remainingCapacity-take
        weights.pop(maxIndex)
        values.pop(maxIndex)
        unitValues.pop(maxIndex)
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    # data = list(map(int, raw_input().split(' ')))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
