# Uses python3
def evalt(a, b, op):
    # provded eval
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    # create seperated arrays
    operators = []
    numbers = []
    
     # fill the arrays
    for i in range(len(dataset)):
        if i%2 == 0:
            numbers.append(dataset[i])
        else:
            operators.append(dataset[i])
    n = len(numbers)
    
    # create the array of 0s 
    MinArr = [[0 for i in range(n)] for j in range(n)]  #minimized values
    MaxArr = [[0 for i in range(n)] for j in range(n)]  #maximized values
    for i in range(n):
        MinArr[i][i] = int(numbers[i])   #so that the tables will look like
        MaxArr[i][i] = int(numbers[i])  #[[i, 0, 0...], [0, i, 0...], [0, 0, i,...]]

    # progress along the right of the martix filling out as we go 
    for s in range(1,n):
        for i in range(0, n-s):
            j = i + s
            MinArr[i][j], MaxArr[i][j] = MinMax(i, j, operators, MaxArr, MinArr)
    # return top right         
    return MaxArr[0][n-1]

def MinMax(i,j, op, MaxArr, MinArr):
    # set min and max to - and + infifity 
    mini = 1000000000
    maxi = -100000000
    # find the computation of all the combos
    for k in range(i, j):
        a = evalt(MaxArr[i][k], MaxArr[k+1][j], op[k])
        b = evalt(MaxArr[i][k], MinArr[k+1][j], op[k])
        c = evalt(MinArr[i][k], MaxArr[k+1][j], op[k])
        d = evalt(MinArr[i][k], MinArr[k+1][j], op[k])
        # create a new min or max accorindly 
        mini = min(mini, a, b, c, d)
        maxi = max(maxi, a, b, c, d)
    # return the min and max    
    return(mini,maxi)     


if __name__ == "__main__":
    # a = "5-8+7*4-8+9"
    # print(get_maximum_value(a))
    print(get_maximum_value(input()))


# help SO explanation https://stackoverflow.com/questions/37101475/dynamic-programming-solution-to-maximizing-an-expression-by-placing-parentheses