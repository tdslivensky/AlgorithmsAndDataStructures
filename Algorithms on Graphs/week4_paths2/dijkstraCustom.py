#Uses python3

import sys
#import queue
import math
import deque 

class Vertex:
    def __init__(self, id):
        self.id = id
        self.visited = False
        self.edges = []
        self.parent = None
        self.distance = math.inf

class Edge:
    def __init__(self, end, wieght):
        self.end = end
        self.weight = wieght

def Parent(num):
    return (num-1)//2

def Left(num):
    return (2 * num) + 1

def Right(num):
    return (2 * num) + 2

def MinHeapify(heap, num, start):
    leftIndex = Left(num)
    rightIndex = Right(num)

    if leftIndex <= start and heap[leftIndex].distance < heap[num].distance:
        smallestIndex = leftIndex
    else:
        smallestIndex = num
    
    if rightIndex <= start and heap[rightIndex].distance < heap[smallestIndex].distance:
        smallestIndex = rightIndex
    
    if smallestIndex != num:
        heap[num], heap[smallestIndex] = heap[smallestIndex], heap[num]
        MinHeapify(heap, smallestIndex, start)

def distance(graph, cost, start, terminal):
    if len(graph) <= 1:
        return -1
    if start == terminal:
        return 0
    graph[start].distance = 0
    #eg = deque(graph.copy())
    eg = graph.copy()
    MinHeapify(eg, 0, len(eg)-1)

    while len(eg) != 0:
        # curr = eg.popleft()
        curr = eg.pop(0)
        graph[curr.id].visited = True
        for edge in curr.edges:
            #evalDist = (graph[curr.id].distance + edge.weight)
            #currDist = graph[edge.end].distance
            if graph[edge.end].distance > (graph[curr.id].distance + edge.weight):
                graph[edge.end].distance = (graph[curr.id].distance + edge.weight)
                graph[edge.end].parent = graph[curr.id].id
                eg.append(graph[edge.end])
        if len(eg != 0):
            MinHeapify(eg, 0, len(eg)-1)
    result = graph[terminal].distance if graph[terminal].distance != math.inf else -1
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [Vertex(i) for i in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].edges.append(Edge((b - 1),w))
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))

# if __name__ == '__main__':
#     # input = sys.stdin.read()
#     # data = list(map(int, input.split()))
#     # n, m = data[0:2]
#     # data = data[2:]
#     # edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
#     # data = data[3 * m:]
#     #edges = [[[1, 2], 1], [[4, 1], 2], [[2, 3], 2], [[1, 3], 5]]
#     #edges = [[[1, 2], 4], [[1, 3], 2], [[2, 3], 2], [[3, 2], 1], [[2, 4], 2], [[3, 5], 4], [[5, 4], 1], [[2, 5], 3], [[3, 4], 4]]
#     #edges = [[[1, 2], 7], [[1, 3], 5], [[2, 3], 2]]
#     #edges =[[[1, 2], 1], [[2, 3], 2], [[1, 3], 5]]
#     edges = []
#     n, m = 5, 4
#     n, m = 5, 9
#     #n, m = 3, 3
#     n, m = 4, 3
#     n, m = 1, 0
#     adj = [Vertex(i) for i in range(n)]
#     cost = [[] for _ in range(n)]
#     for ((a, b), w) in edges:
#         adj[a - 1].edges.append(Edge((b - 1),w))
#         cost[a - 1].append(w)
#     # s, t = data[0] - 1, data[1] - 1
#     s, t = 2, 2
#     s, t = 0, 0
#     #s, t = 0, 4
#     #s, t = 2, 1
#     print(distance(adj, cost, s, t))
