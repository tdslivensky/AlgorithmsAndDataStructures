# python3
import sys

# more detail in ascHeapSort
def Parent(num):
    return (num-1)//2

def Left(num):
    return (2 * num) + 1

def Right(num):
    return (2 * num) + 2

def MinHeapify(heap, num, swaps):
    leftIndex = Left(num)
    rightIndex = Right(num)
    start = len(heap)-1
    if leftIndex <= start and heap[leftIndex] < heap[num]:
        smallestIndex = leftIndex
    else:
        smallestIndex = num
    
    if rightIndex <= start and heap[rightIndex] < heap[smallestIndex]:
        smallestIndex = rightIndex
    
    if smallestIndex != num:
        # to track swaps we simply add to that array  every time a smal is made 
        heap[num], heap[smallestIndex] = heap[smallestIndex], heap[num]
        swaps.append((num,smallestIndex))
        MinHeapify(heap, smallestIndex, swaps)

def BuildMinHeap(arr):
    start = len(arr)//2
    swaps = []
    # start at the 1/2 way point and build a heap keeping track of swaps
    for i in range(start, -1,-1):
        MinHeapify(arr, i, swaps)
    return swaps  


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    # data = [5,4,3,2,1]
    # data.reverse()
    swaps = BuildMinHeap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
