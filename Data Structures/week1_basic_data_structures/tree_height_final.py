# python3

import sys
import threading

class Node:
    def __init__(self,value = None):
        self.Next = value
        self.ParentPointer = None
        self.Children = []
        self.Root = False

    def AddChildren(self, child):
        self.Children.append(child)

def CreateNodes(n,parents):
    # create an array fo nodes
    nodes = []
    # every node added with a pointer to parents 
    for i in range(n):
        nody = Node(i)
        nodes.append(nody)
        nodes[i].ParentPointer = parents[i]
    return nodes

def CreateTree(nodes):
    Final = 0
    # create an array of arrays for each node
    for i in range(len(nodes)):
        parent = nodes[i].ParentPointer
        CurrentNode = nodes[i]
        if parent == -1:
            CurrentNode.Root = True
            Final = i
        else:
            nodes[CurrentNode.ParentPointer].AddChildren(CurrentNode)
    # only return the root as it has everyone        
    return nodes[Final]

def FinalComputation(n, parents):
    # handel edges
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    nodes = CreateNodes(n, parents)
    root = CreateTree(nodes)
    depth = compute_height(root)

    return depth

def compute_height(node):
    if node == None:
        return 0
    # RECURR  down the tree adding 1 each time but only increasing the maxdepth if it is greater works for unbalances
    maxValue = 0
    for n in node.Children:
        depth = compute_height(n)
        if depth > maxValue:
            maxValue = depth
    
    return maxValue + 1

     # idk you could do a queue
     #    
    # while len(Queue) != 0:
    #     curr = Queue.pop(0)
    #     childrenLevel += 
    #     for i in range(len(curr.Children)):
    #         Queue.append(curr.Children[i])

    # # Replace this code with a faster implementation
    # max_height = 0
    # for vertex in range(n):
    #     height = 0
    #     current = vertex
    #     while current != -1:
    #         height += 1
    #         current = parents[current]
    #     max_height = max(max_height, height)
    # return max_height
    # return True


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    # print(compute_height(n, parents))
    # n = 5
    # parents = [-1,0,4,0,3]
    print(FinalComputation(n,parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
