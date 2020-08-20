#Uses python3

import sys
class node():
    def __init__(self, visited, edges):
        self.preOrder = None
        self.postOrder = None
        self.visited = visited
        self.edges = edges 
        self.eval = False

class time():
    def __init__(self, time):
        self.time = time
        self.acyclic = 0
        self.order = []


def dfs(adj, x, order):
    adj[x].visited = True
    adj[x].eval = True
    adj[x].preOrder = order.time
    order.time += 1
    for vertex in adj[x].edges:
        if adj[vertex].visited == False:
            dfs(adj, vertex, order)
        elif adj[vertex].visited == True and adj[vertex].eval == True:
            order.acyclic = 1
    adj[x].postOrder = order.time 
    adj[x].eval = False
    order.order.insert(0, x)    
    order.time += 1


def toposort(adj):
    #used = [0] * len(adj)
    order = time(1)
    for i in range(len(adj)):
        if adj[i].visited == False:
            dfs(adj, i, order) 
    #write your code here
    return order.order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [node(False, []) for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].edges.append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

# if __name__ == '__main__':
#     #input = sys.stdin.read()
#     #data = list(map(int, input.split()))
#     #n, m = data[0:2]
#     #data = data[2:]
#     #edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
#     n, m = 4, 3
#     n, m = 4, 1
#     edges = [[1,2],[4,1],[3,1]]
#     edges =[[3,1]]
#     adj = [node(False, []) for _ in range(n)]
#     for (a, b) in edges:
#         adj[a - 1].edges.append(b - 1)
#     order = toposort(adj)
#     for x in order:
#         print(x + 1, end=' ')

