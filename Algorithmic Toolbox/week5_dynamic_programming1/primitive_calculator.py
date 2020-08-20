# Uses python3
import sys

def optimal_sequence(n):
    Change = {0:0}
    l = []
    # setting up dict
    for m in range(1,n+1):
        # sets a base for comparision
        if m not in Change:
            # least number of ops to get somewher is division if the module if 0
            if m%3 == 0:
                Change[m] = m/3
            elif m%2 == 0:
                Change[m] = m/2
            else:
                # otherwise its just 1 + the previous
                Change[m] = Change[m-1] + 1
        arr = [1, 2, 3]           
        for i in range(0,len(arr)):
            # for first operation previous + 1
            if i == 0:
                numCoins = Change[m-arr[i]] + 1
            # otherwise its the m%2 + 1    
            elif i == 1 and m%2 == 0:
                numCoins = Change[m/2] + 1
            # otherwise its the m%3 + 1
            elif i == 2 and m%3 == 0:
                numCoins = Change[m/3] + 1
            # eval each to get the minumum moves     
            if numCoins < Change[m]:
                Change[m] = numCoins

    # result is a dict with the min operations to get to the number

    # create the backtrace
    num = n
    l.append(num)
    while num != 1:
        a = {}

        # populate a dict with the possible value back from the num 
        if num%3 == 0 and num%2 == 0:
            a[int(num-1)] = Change[num-1]
            a[int(num/2)] = Change[num/2]
            a[int(num/3)] = Change[num/3]
        elif num%3 == 0 and num%2 != 0:
            a[int(num-1)] = Change[num-1]
            a[int(num/3)] = Change[num/3]
        elif num%3 != 0 and num%2 == 0:
            a[int(num-1)] = Change[num-1]
            a[int(num/2)] = Change[num/2]
        else:
            a[int(num-1)] = Change[num-1]
        

        # handel what to do when the options are all one action from the end 
        if 2 in a and 3 in a:
            if num%3 == 0:
                num = 3
            else:
                num = 2
        elif (2 in a or 3 in a) and 1 in a:
            num = 1        
        else:
            # otherwise the num we want to ge to is the min of the thing in the dict
            # set new num
            num = min(a, key = a.get)
        # put num into array    
        l.append(num)

    # reverse the order so it is ascending 
    return reversed(l)

# input = sys.stdin.read()
# n = int(input)
n = 99
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
