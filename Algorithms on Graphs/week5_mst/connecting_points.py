#Uses python3
import sys
import math
import heapq
import queue

class Vertex():
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.popped = False
        self.parent = id
        self.weight = math.inf
    
    def __lt__(self, other):
        return self.weight < other.weight



def minimum_distance(x, y):
    result = 0.00000000000000000000
    v = []
    if len(x) == 0:
        return result
    for i in range(len(x)):
        v.append(Vertex(i,x[i],y[i]))
    
    v[0].weight = 0

    qAlpha = v.copy()
    heapq.heapify(qAlpha)

    while len(qAlpha) != 0:
        curr = heapq.heappop(qAlpha)
        result += curr.weight
        qBeta = []
        v[curr.id].popped = True
        for node in qAlpha:
            edgeWeight = DetermineWeight(curr,node)
            if node.popped == False and edgeWeight < node.weight:
                v[node.id].parent = curr.id
                v[node.id].weight = edgeWeight
                qBeta.append(v[node.id]) 
            else:
                qBeta.append(v[node.id])
        
        qAlpha = qBeta.copy()
        heapq.heapify(qAlpha)
    return result

def DetermineWeight(start, end):
    x = start.x - end.x
    y = start.y - end.y
    r = math.sqrt((math.pow(x, 2) + math.pow(y,2)))
    return r


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))

# if __name__ == '__main__':
#     data = [4, 0, 0, 0, 1, 1, 0, 1, 1] #3
#     data = [5, 0, 0, 0, 2, 1, 1, 3, 0, 3, 2] #7.064495102
#     data = [4, 1, 1, -1, -1, 1, -1, -1, 1] #6
#     data = [0]
#     n = data[0]
#     x = data[1::2]
#     y = data[2::2]
#     print("{0:.9f}".format(minimum_distance(x, y)))















# def minimum_distance(x, y):
#     result = 0.0
#     v = []

#     for i in range(len(x)):
#         v.append(Vertex(i,x[i],y[i]))
    
#     v[0].weight = 0

#     qAlpha = queue.PriorityQueue(v.copy())
#     qBeta = queue.PriorityQueue()

#     while not qAlpha.empty():
#         curr = qAlpha.get()
#         result += curr.weight
#         qBeta = queue.PriorityQueue()
#         v[curr.id].popped = True

#         for node in qAlpha:
#             edgeWeight = DetermineWeight(curr,node)
#             if edgeWeight < node.weight:
#                 v[node.id].parent = curr.id
#                 v[node.id].weight = edgeWeight
#                 qBeta.put(v[node.id]) 
#             else:
#                 qBeta.put(v[node.id])
        
#         qAlpha = queue.PriorityQueue(qBeta.copy())

#     return result