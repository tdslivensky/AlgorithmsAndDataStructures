#Uses python3

import sys

sys.setrecursionlimit(200000)

class node():
    def __init__(self, visited, edges, edgesReversed, Id):
        self.preOrder = None
        self.postOrder = None
        self.Id = Id
        self.visited = visited
        self.edges = edges 
        self.edgesReversed = edgesReversed
        self.eval = False

class time():
    def __init__(self, time):
        self.time = time
        self.acyclic = 0
        #self.order = []

def dfs(adj, x, order):
    adj[x].visited = True
    adj[x].eval = True
    adj[x].preOrder = order.time
    order.time += 1
    for vertex in adj[x].edgesReversed:
        if adj[vertex].visited == False:
            dfs(adj, vertex, order)
        elif adj[vertex].visited == True and adj[vertex].eval == True:
            order.acyclic = 1
    adj[x].postOrder = order.time 
    adj[x].eval = False
    #order.order.insert(0, x)    
    order.time += 1

def explore(adj, x, order):
    adj[x].visited = True
    for vertex in adj[x].edges:
        if adj[vertex].visited == False:
            explore(adj, vertex, order)

def number_of_strongly_connected_components(adj):
    result = 0

    order = time(1)
    for i in range(len(adj)):
        if adj[i].visited == False:
            dfs(adj, i, order)
    
    for vert in adj:
        vert.visited = False
    
    #adj.sort(key=lambda x: x.postOrder, reverse=True)
    sortedAdj = sorted(adj, key=lambda x: x.postOrder, reverse=True)

    for i in range(len(sortedAdj)):
        if adj[sortedAdj[i].Id].visited == False:
            explore(adj, sortedAdj[i].Id, order)
            result += 1

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [node(False, [], [], i) for i in range(n)]
    for (a, b) in edges:
        adj[a - 1].edges.append(b - 1)
        adj[b - 1].edgesReversed.append(a - 1)
    print(number_of_strongly_connected_components(adj))

# if __name__ == '__main__':
#     #n, m = 4, 4
#     #edges = [[1,2], [4,1], [2,3], [3,1]]
#     n, m = 5, 7
#     edges = [[2,1], [3,2], [3,1], [4,3], [4,1], [5,2], [5,3]]
#     adj = [node(False, [], [], i) for i in range(n)]
#     for (a, b) in edges:
#         adj[a - 1].edges.append(b - 1)
#         adj[b - 1].edgesReversed.append(a - 1)
#     print(number_of_strongly_connected_components(adj))
