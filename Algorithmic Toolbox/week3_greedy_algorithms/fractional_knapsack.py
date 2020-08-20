# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    TotalWeight = capacity
    value = 0
    weightValueIndex = 0
    arr = [0] * len(weights)
    # write your code here
    # place all the weigts into a array with a sub array of [weigth, value, weight/value]
    for i in range(len(weights)):
        WeightPerValue = values[i]/weights[i]
        arr[i] = [weights[i],values[i],WeightPerValue]

    # sort the arr by weight/value
    a = sorted(arr, key=lambda x:float(x[2]), reverse=True)
    
    # while room is open
    while(TotalWeight != 0):
        # if there is only one item
        if(len(weights)==1):
            # and the space is more than the items weight take the whole item
            if(TotalWeight > a[weightValueIndex][0]):
                value = a[weightValueIndex][1]
                return value
            # else take a faction of the item
            else:
                value += (TotalWeight * a[weightValueIndex][2])
                return value
        # same as above for mulitple weights        
        elif(TotalWeight > a[weightValueIndex][0]):
            TotalWeight -= a[weightValueIndex][0]
            value += a[weightValueIndex][1]
            weightValueIndex += 1
        else:
            value += (TotalWeight * a[weightValueIndex][2])
            TotalWeight = 0

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
