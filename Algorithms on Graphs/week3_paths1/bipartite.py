#Uses python3

import sys
import queue
from collections import deque

class Vertex():
    def __init__(self, edges):
        #self.visited = False
        self.edges = edges
        self.distance = None
        self.color = None

class Bipart(self):
    def __init__(self):
        self.bipartite = False

def bipartite(adj):
    #write your code here
    bipart = Bipart()
    BreathFirstSearch(adj, 0, bipart)
    return -1

def BreathFirstSearch(graph, start, bipart):
    graph[start].distance = 0
    graph[start].color = 'white'
    q = deque()
    q.append(graph[start])
    while len(q) != 0:
        currentVertx = q.popleft()
        c = 'white' if currentVertx.color == 'black' else 'black' 
        for vertIndex in currentVertx.edges:
            if graph[vertIndex].distance == None:
                graph[vertIndex].distance = currentVertx.distance + 1
                graph[vertIndex].color = c
                q.append(graph[vertIndex])
            elif graph[vertIndex].distance != None: 
                if graph[vertIndex].color == graph[currentVertx].color:
                    bipart.bipartite = True
            
# maybe use DFS to prove acyclicity

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
