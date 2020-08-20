# Uses python3
import sys

def optimal_weight(weight, arr):
    # create an array of arrays 
    A = [0] * (len(arr) + 1)
    for k in range(len(A)):
        A[k] = ([0] * (weight+1))
    # write your code here

    # rows and columns loops
    for i in range (1,len(arr)+1):
        for w in range(1,weight+1):
            # best value is either the IV which is the value above the current
            InnitialValue = A[i-1][w]
            # or if the w if greater that means the item was added 
            if w >= arr[i-1]:
                # so the comparision is between adding from the previous value and not 
                SecondValue = A[i-1][w-arr[i-1]] + arr[i-1]
                A[i][w] = max(InnitialValue, SecondValue)
            else:
                A[i][w] = InnitialValue 
    # return the max number of movements 
    return A[len(arr)][weight]

# extra backtrace code unused
def added_numbers(weight, arr):
    BoolArr = {}
    num = weight
    index = len(arr)

    # set up arrays
    A = [0] * (len(arr) + 1)
    for k in range(len(A)):
        A[k] = ([0] * (weight+1))

    # do the same evaluation
    for i in range (1,len(arr)+1):
        for w in range(1,weight+1):
            InnitialValue = A[i-1][w]
            if w >= arr[i-1]:
                SecondValue = A[i-1][w-arr[i-1]] + arr[i-1]
            A[i][w] = max(InnitialValue, SecondValue)

    # loop backwards # we know if the values match the number wasn't used otherwise we need to move up and over.
    while num > 1:
        if A[index-1][num] == A[index][num]:
            BoolArr[arr[index-1]] = False
            index -= 1
        else:
            BoolArr[arr[index-1]] = True
            index -= 1
            num -= arr[index]

    return BoolArr        




if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

    #W = the max weigth 
    #w = the array of weights
    # W = 10
    # w = [8,4,1]
    # print(optimal_weight(W, w))
