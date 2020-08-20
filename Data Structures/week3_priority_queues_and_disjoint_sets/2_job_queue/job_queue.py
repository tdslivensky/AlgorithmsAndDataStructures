# python3
import sys
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
Worker = namedtuple("Worker",["core","ending_time"])

def Parent(num):
    return (num-1)//2

def Left(num):
    return (2 * num) + 1

def Right(num):
    return (2 * num) + 2

def MinHeapify(heap, num, start):
    leftIndex = Left(num)
    rightIndex = Right(num)
    smallestIndex = num

    if leftIndex <= start and heap[leftIndex][1] < heap[smallestIndex][1]:
        smallestIndex = leftIndex

    
    if rightIndex <= start and heap[rightIndex][1] <= heap[smallestIndex][1]:
        if heap[rightIndex][1] < heap[smallestIndex][1]:
            smallestIndex = rightIndex
        else:
            if heap[rightIndex][0] < heap[smallestIndex][0]:
                smallestIndex = rightIndex
                

    if smallestIndex != num:
        heap[num], heap[smallestIndex] = heap[smallestIndex], heap[num]
        MinHeapify(heap, smallestIndex, start)

def BuildMinHeap(arr):
    start = len(arr)//2
    for i in range(start, -1,-1):
        MinHeapify(arr, i, len(arr)-1)  

def assign_jobs(n_workers, jobs):
    result = []
    next_free_time = []
    for i in range(n_workers):
        next_free_time.append([i,0])

    for job in jobs:
        end = 0
        tup = next_free_time[0]
        result.append(AssignedJob(tup[0], tup[1]))
        end = next_free_time[0][1] + job
        next_free_time[0][1] = end
        MinHeapify(next_free_time, 0, len(next_free_time)-1)

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs
    #n_workers = 4
    #jobs = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]
    #jobs = [1,2,3,4,5]
    #jobs = [2, 3, 1, 4, 5, 9, 8, 1, 9]
    assigned_jobs = assign_jobs(n_workers, jobs)
    assigned_jobs = sorted(assigned_jobs, key=lambda x: (x.started_at, x.worker))
    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()

#https://stackoverflow.com/questions/22900388/why-in-a-heap-implemented-by-array-the-index-0-is-left-unused