#uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []
        self.optimalWeight = -1
        self.onStack = False
        self.solved = False


def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for _ in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def dfs(tree, vertex, parent):
    if tree[vertex].solved == True:
        return tree[vertex].optimalWeight
    
    # weights of children and grandchildren
    childWeights = 0
    # parent + grandchildren weight
    grandChildrenWeight = tree[vertex].weight
    tree[vertex].onStack == True

    # leaves
    exploredChildrenSet = {tree[child].onStack for child in tree[vertex].children}
    if False not in exploredChildrenSet:
        tree[vertex].onStack = False
        tree[vertex].solved = True
        tree[vertex].optimalWeight = tree[vertex].weight
        return tree[vertex].weight

    # recursing on grandchildren
    for child in tree[vertex].children:
        if tree[child].onStack == False:
            for grandChild in tree[child].children:
                if child != grandChild and grandChild != parent and not tree[grandChild].onStack:
                    tree[child].onStack = True
                    result = dfs(tree, grandChild, child)
                    grandChildrenWeight += result
            tree[child].onStack = False
    
    for child in tree[vertex].children:
        if child != parent and not tree[child].onStack:
            result = dfs(tree, child, vertex)
            childWeights += result

    tree[vertex].onStack = False
    tree[vertex].solved = True
    tree[vertex].optimalWeight = max(childWeights, grandChildrenWeight)

    return tree[vertex].optimalWeight




def MaxWeightIndependentTreeSubset(tree, vertex, parent):
    size = len(tree)
    if size == 0:
        return 0
    return dfs(tree, 0, -1)


def main():
    tree = ReadTree()
    weight = MaxWeightIndependentTreeSubset(tree, 0, -1)
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()

    # for child in tree[vertex].children:
    #     if child != parent:
    #         dfs(tree, child, vertex)

    # # This is a template function for processing a tree using depth-first search.
    # # Write your code here.
    # # You may need to add more parameters to this function for child processing.