#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self, num, nodes):
    self.n = num
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    self.IsBST = True
    for i in range(self.n):
        self.key[i] = nodes[i][0]
        if nodes[i][1] == -1:
            self.left[i] = -1
        else:
            self.left[i] = nodes[i][1]
        if nodes[i][2] == -1:
            self.right[i] = -1
        else:
            self.right[i] = nodes[i][2]

  def InOrderWalk(self, r, arr, i):
    if i != -1:
        self.InOrderWalk(self.key[self.left[i]], arr, self.left[i])
        a = self.left[i]
        b = self.key[self.left[i]] if a != None else -1
        c = self.right[i]
        if a == -1 and c == -1:
            arr.append(self.key[i])
        elif a == -1 and self.key[c] >= self.key[i]:
            arr.append(self.key[i])
        elif self.key[a] < self.key[i] and c == -1:
            arr.append(self.key[i])
        elif self.key[a] < self.key[i] and self.key[c] >= self.key[i]:
            arr.append(self.key[i])
        else:
            self.IsBST = False
        self.InOrderWalk(self.key[self.right[i]], arr, self.right[i])
       
  def inOrder(self):
    self.result = []
    self.i = 0
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.InOrderWalk(self.key[self.i], self.result, self.i)

    if self.IsBST == False:
        return False
    else:
        for i in range(len(self.result)-1):
            if self.result[i] > self.result[i+1]:
                return False
    return True

def IsBinarySearchTree(tree):
    t = TreeOrders()
    t.read(len(tree), tree)
    return t.inOrder()

def main():
    #nodes = 3
    #a = ['2 1 2','1 -1 -1','3 -1 -1']
    #a = ['1 1 2', '2 -1 -1', '3 -1 -1']
    #nodes = 5
    #a = ['1 -1 1', '2 -1 2', '3 -1 3', '4 -1 4', '5 -1 -1']
    #nodes = 7
    #a = ['4 1 2','2 3 4','6 5 6','1 -1 -1','3 -1 -1','5 -1 -1','7 -1 -1']
    #nodes = 4
    #a = ['4 1 -1','2 2 3','1 -1 -1','5 -1 -1']
    #nodes = 3
    #a = ['2 1 2', '2 -1 -1', '4 -1 -1']
    #nodes = 1
    #a = ['2147483647 -1 -1']
    nodes = int(sys.stdin.readline().strip())
    if nodes == 0:
        print("CORRECT")
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
        #tree.append(list(map(int, a[i].split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
