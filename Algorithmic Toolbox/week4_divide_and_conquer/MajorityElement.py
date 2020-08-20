# Uses python3
import sys
import collections

def get_majority_element(a, left, right):
    #create a count of every grouping
    array = collections.Counter(a)
    # find max count
    maximum = max(array.keys(), key=array.get)
    # determine is count over half 
    if(array[maximum] > len(a)//2):
        return array[maximum]
    else:
        return -1    


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)