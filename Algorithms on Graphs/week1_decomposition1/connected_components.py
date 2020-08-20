#Uses python3

import sys

class node():
    def __init__(self, visited, number, edges):
        self.visited = visited
        self.number = number
        self.edges = edges



def number_of_components(adj):
    result = 0
    
    for i in range(len(adj)):
        if adj[i].visited == False:
            result += 1
            explore(adj, i, result) 

    return result

def explore(adj, x, island):
    adj[x].visited = True
    adj[x].number = island
    for vertex in adj[x].edges:
        if adj[vertex].visited == False:
            explore(adj, vertex, island)
    return adj

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [node(False,0,[]) for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].edges.append(b - 1)
        adj[b - 1].edges.append(a - 1)
    print(number_of_components(adj))

# if __name__ == '__main__':
#     #input = sys.stdin.read()
#     #data = list(map(int, input.split()))
#     #n, m = data[0:2]
#     n, m = 4, 2
#     #data = data[2:]
#     #edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
#     edges = [[1,2], [3,2]]
#     adj = [node(False,0,[]) for _ in range(n)]
#     for (a, b) in edges:
#         adj[a - 1].edges.append(b - 1)
#         adj[b - 1].edges.append(a - 1)
#     print(number_of_components(adj))
