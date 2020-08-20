#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size
class TreeOrders:
  def read(self, num, nodes):
    self.n = num
    #self.n = 5
    #self.arr = ['4 1 2','2 3 4','5 -1 -1','1 -1 -1','3 -1 -1'] #, '10 -1 -1', '7 -1 -1']
    #self.n = 10
    #self.arr = ['0 7 2','10 -1 -1','20 -1 6','30 8 9','40 3 -1','50 -1 -1','60 1 -1','70 5 4','80 -1 -1','90 -1 -1']
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]

    for i in range(self.n):
      #[a, b, c] = map(int, nodes[i].split())
      #[a, b, c] = map(int, self.arr[i].split())
      self.key[i] = nodes[i][0]
      self.left[i] = nodes[i][1]
      self.right[i] = nodes[i][2]

  def InOrderWalk(self, r, arr, i):
    if i != -1:
      self.InOrderWalk(self.key[self.left[i]], arr, self.left[i])
      arr.append(self.key[i])
      self.InOrderWalk(self.key[self.right[i]], arr, self.right[i])
       
  def inOrder(self):
    self.result = []
    self.i = 0
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.InOrderWalk(self.key[self.i], self.result, self.i)         
    return self.result

def IsBinarySearchTree(tree):
  t = TreeOrders()
  t.read(len(tree), tree)
  inOrder = t.inOrder()

  for i in range(len(inOrder)-1):
    if inOrder[i] > inOrder[i+1]:
      return False
  return True


def main():
  #nodes = 3
  #a = ['2 1 2','1 -1 -1','3 -1 -1']
  #a = ['1 1 2', '2 -1 -1', '3 -1 -1']
  # nodes = 5
  # a = ['1 -1 1', '2 -1 2', '3 -1 3', '4 -1 4', '5 -1 -1']
  # nodes = 7
  # a = ['4 1 2','2 3 4','6 5 6','1 -1 -1','3 -1 -1','5 -1 -1','7 -1 -1']
  # nodes = 4
  # a = ['4 1 -1','2 2 3','1 -1 -1','5 -1 -1']
  # nodes = 3
  # a = ['2 1 2', '1 -1 -1', '2 -1 -1']
  nodes = int(sys.stdin.readline().strip())
  if nodes == 0:
    print("CORRECT")
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, a[i].split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
