# python3
import sys

class Heap():
    def __init__(self, arr):
        self.arr = arr
        self.heapSize = 0
     
def Parent(num):
    return num//2

def Left(num):
    return 2 * num

def Right(num):
    return (2 * num) + 1

def MaxHeapify(heap, num):
    leftIndex = Left(num)
    rightIndex = Right(num)

    if leftIndex <= heap.heapSize and heap.arr[leftIndex] > heap.arr[num]:
        largestIndex = leftIndex
    else:
        largestIndex = num
    
    if rightIndex <= heap.heapSize and heap.arr[rightIndex] > heap.arr[largestIndex]:
        largestIndex = rightIndex
    
    if largestIndex != num:
        heap.arr[num], heap.arr[largestIndex] = heap.arr[largestIndex], heap.arr[num]
        MaxHeapify(heap, largestIndex)

def BuildMaxHeap(arr):
    h = Heap(arr)
    h.size = len(arr)
    start = len(arr)//2
    for i in range(start, 0, -1):
        MaxHeapify(h, i)
    return h

def HeapSort(arr):
    heap = BuildMaxHeap(arr)
    start = heap.size - 1 
    for i in range(start,1,-1):
        heap.arr[0], heap.arr[i] = heap.arr[i], heap.arr[0]
        heap.size -= 1
        MaxHeapify(heap,0)

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

    data = [5,4,3,2,1,9]
    n = len(data)
    HeapSort()
    # print(len(swaps))
    # for i, j in swaps:
    #     print(i, j)


if __name__ == "__main__":
    main()
