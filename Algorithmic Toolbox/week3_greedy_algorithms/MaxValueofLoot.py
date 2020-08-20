
def get_optimal_value(capacity, weights, values):
    TotalWeight = capacity
    value = 0
    weightValueIndex = 0
    arr = [0] * len(weights)
    # write your code here
    for i in range(len(weights)):
        WeightPerValue = values[i]/weights[i]
        arr[i] = [weights[i],values[i],WeightPerValue]

    a = sorted(arr, key=lambda x:float(x[2]), reverse=True)
    
    while(TotalWeight != 0):
        if(len(weights)==1):
            if(TotalWeight > a[weightValueIndex][0]):
                value = a[weightValueIndex][1]
                return value
            else:
                value += (TotalWeight * a[weightValueIndex][2])
                return value
        elif(TotalWeight > a[weightValueIndex][0]):
            TotalWeight -= a[weightValueIndex][0]
            value += a[weightValueIndex][1]
            weightValueIndex += 1
        else:
            value += (TotalWeight * a[weightValueIndex][2])
            TotalWeight = 0

    return value

if __name__ == "__main__":
    capacity = 10
    values = [500]
    weights = [30]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))