# python3
import sys

# class Heap():
#     def __init__(self, arr):
#         self.arr = arr
#         self.heapSize = 0

# get the parent of the index
def Parent(num):
    return (num-1)//2

# get left child of index
def Left(num):
    return (2 * num) + 1

# get right child of index
def Right(num):
    return (2 * num) + 2

# recursively create max heap tree 
# take an array heap, the index to evaluate, and the max range of the heap
def MaxHeapify(heap, num, start):
    # get index of left and right child
    leftIndex = Left(num)
    rightIndex = Right(num)

    # trying to determin if the left or right is greater than the parent
    # if left in range and the left is the largest index
    if leftIndex <= start and heap[leftIndex] > heap[num]:
        largestIndex = leftIndex
    else:
        largestIndex = num
    
    # if right in range and the right is the largest index
    if rightIndex <= start and heap[rightIndex] > heap[largestIndex]:
        largestIndex = rightIndex
    
    # if the parent is not the the largest number 
    if largestIndex != num:
        # swap larger for parent
        heap[num], heap[largestIndex] = heap[largestIndex], heap[num]
        # and heapify the largest index to ensure the swap did cause issues
        MaxHeapify(heap, largestIndex, start)

def BuildMaxHeap(arr):
    # start at the half way point to ensure all point have leaves 
    start = len(arr)//2
    # got from  the 1/2 way point down (ie furestest parent to root)
    for i in range(start, -1,-1):
        MaxHeapify(arr, i, len(arr)-1)   

def MaxHeapSort(arr):
    BuildMaxHeap(arr)
    # start at end
    start = len(arr) - 1 
    #take out root as biggest number and remake heap
    for i in range(start,0,-1):
        arr[0], arr[i] = arr[i], arr[0]
        #end = start - 1
        MaxHeapify(arr, 0, i-1)

# junk
def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def main():
    # n = int(input())
    # data = list(map(int, input().split()))
    # assert len(data) == n

    # swaps = build_heap(data)

    data = [5,6,3,2,1,9]
    MaxHeapSort(data)
    # print(len(swaps))
    # for i, j in swaps:
    #     print(i, j)
    for i in data:
        print(i)


if __name__ == "__main__":
    main()
