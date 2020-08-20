# Uses python3
import sys
import random

def partition3(a, l, r):
    # the value that we are comparing to to see equality 
    x = a[l]
    # counter to ensure we track the range of the eqaulity
    j = l
    k = l


    for i in range(l+1, r+1):
        # if the value at i == x then we advance the eqaulity max counter k and swap k and i
        if a[i] == x:
            k += 1
            a[i], a[k] = a[k], a[i]
        # otherwise the item needs to be moved belwo the equality range
        elif a[i] < x:
            # increase both counters
            j+=1
            k+=1
            # swap i with the bottom of the eqaulity range so the low num is in place and the matching number is at i
            a[i], a[j] = a[j], a[i]
            # if we are in a position were an eqaulity range exists 
            if j != k:
                # swap i with k  to move the matching number into the eqaulity range
                a[i], a[k] = a[k], a[i]
        #if neither of these thing happend its larger that the equaliy and can be left there        
    a[l], a[j] = a[j], a[l]
    return [j,k]

# def partition2(a, l, r):
#     x = a[l]
#     j = l
#     for i in range(l + 1, r + 1):
#         if a[i] <= x:
#             j += 1
#             a[i], a[j] = a[j], a[i]
#     a[l], a[j] = a[j], a[l]
#     return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
       # select a random index between l and r 
    k = random.randint(l, r)
    # swap low index point with random point 
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition3(a, l, r)
    # recursively call on the sectoins that are outside the partition b/c the partion range are all equal numbers
    randomized_quick_sort(a, l, m[0] - 1)
    randomized_quick_sort(a, m[1] + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')