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
        self.optimal_weight = -1
        self.on_stack = False
        self.solved = False

def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    # print([v.children for v in tree])
    return tree

def dfs(tree, vertex, parent):
    if tree[vertex].solved:
        return tree[vertex].optimal_weight
    child_weights = 0 # combined weight of children and their grandchildren
    grand_child_weights = tree[vertex].weight #combined weight of parent + grandchildren
    tree[vertex].on_stack = True

    # leaf conditional
    explored_children_set = {tree[child].on_stack for child in tree[vertex].children}
    if False not in explored_children_set:
        tree[vertex].on_stack = False
        tree[vertex].solved = True
        tree[vertex].optimal_weight = tree[vertex].weight
        return tree[vertex].weight

    # recurse on grandchildren
    for child in tree[vertex].children:
        if not tree[child].on_stack:
            for grand_child in tree[child].children:

                if child != grand_child and grand_child != parent and not tree[grand_child].on_stack:
                    tree[child].on_stack = True
                    result = dfs(tree, grand_child, child)
                    grand_child_weights += result
            tree[child].on_stack = False

    for child in tree[vertex].children:
        if child != parent and not tree[child].on_stack:
            result = dfs(tree, child, vertex)
            child_weights += result

    tree[vertex].on_stack = False
    tree[vertex].solved = True
    tree[vertex].optimal_weight = max(child_weights, grand_child_weights)
    return tree[vertex].optimal_weight

def MaxWeightIndependentTreeSubset(tree, vertex, parent):
    size = len(tree)
    if size == 0:
        return 0
    return dfs(tree, 0, -1)

def main():
    tree = ReadTree()
    # print(tree)
    weight = MaxWeightIndependentTreeSubset(tree, 0, -1)
    # print([v.children for v in tree])
    # print([v.optimal_weight for v in tree])
    print(weight)


# This is to avoid stack overflow issues
# main()
threading.Thread(target=main).start()