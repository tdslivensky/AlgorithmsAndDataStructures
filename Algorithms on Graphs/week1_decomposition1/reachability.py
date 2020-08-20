#Uses python3

import sys

def reach(adj, x, y):
    explore(adj,x)
    if adj[y][0] == True:
        return 1     
    return 0

def explore(adj, x):
    adj[x][0] = True
    for vertex in adj[x][1]:
        if adj[vertex][0] == False:
            explore(adj, vertex)
    return adj

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[False,[]] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1][1].append(b - 1)
        adj[b - 1][1].append(a - 1)
    print(reach(adj, x, y))

# if __name__ == '__main__':
#     #input = sys.stdin.read()
#     #data = list(map(int, input.split()))
#     n, m = 4, 4
#     #n, m = 4, 2
#     #data = data[2:]
#     #edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
#     edges = [[1,2],[3,2],[4,3],[1,4]]
#     #edges = [[1,2], [3,2]]
#     #x, y = data[2 * m:]
#     adj = [[False,[]] for _ in range(n)]
#     #x, y = x - 1, y - 1
#     x = 0 
#     y = 3
#     #adj = [[False,[1,3]], [False,[0,2]], [False,[1,3]], [False,[2,0]]]
#     for (a, b) in edges:
#         adj[a - 1][1].append(b - 1)
#         adj[b - 1][1].append(a - 1)
#     print(reach(adj, x, y))
