# python3
import sys

#see ascHeap sort for description
     
def Parent(num):
    return (num-1)//2

def Left(num):
    return (2 * num) + 1

def Right(num):
    return (2 * num) + 2

def MinHeapify(heap, num, start):
    leftIndex = Left(num)
    rightIndex = Right(num)

    if leftIndex <= start and heap[leftIndex] < heap[num]:
        smallestIndex = leftIndex
    else:
        smallestIndex = num
    
    if rightIndex <= start and heap[rightIndex] < heap[smallestIndex]:
        smallestIndex = rightIndex
    
    if smallestIndex != num:
        heap[num], heap[smallestIndex] = heap[smallestIndex], heap[num]
        MinHeapify(heap, smallestIndex, start)

def BuildMinHeap(arr):
    start = len(arr)//2
    for i in range(start, -1,-1):
        MinHeapify(arr, i, len(arr)-1)   

def MinHeapSort(arr):
    BuildMinHeap(arr)
    start = len(arr) - 1 
    for i in range(start,0,-1):
        arr[0], arr[i] = arr[i], arr[0]
        MinHeapify(arr, 0, i-1)

def build_heap(data):
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
    MinHeapSort(data)
    # print(len(swaps))
    # for i, j in swaps:
    #     print(i, j)
    for i in data:
        print(i)


if __name__ == "__main__":
    main()
