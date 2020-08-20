# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    #self.n = 5
    #self.arr = ['4 1 2','2 3 4','5 -1 -1','1 -1 -1','3 -1 -1'] #, '10 -1 -1', '7 -1 -1']
    #self.n = 10
    #self.arr = ['0 7 2','10 -1 -1','20 -1 6','30 8 9','40 3 -1','50 -1 -1','60 1 -1','70 5 4','80 -1 -1','90 -1 -1']
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    self.nodes = []
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      #[a, b, c] = map(int, self.arr[i].split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c
    
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

  def PreOrderWalk(self, r, arr, i):
    if i != -1:
      arr.append(self.key[i])
      self.PreOrderWalk(self.key[self.left[i]], arr, self.left[i])
      self.PreOrderWalk(self.key[self.right[i]], arr, self.right[i])

  def preOrder(self):
    self.result = []
    self.i = 0
    # Finish the implementation
    # You may need to add a new recursive method to do that 
    self.PreOrderWalk(self.key[self.i], self.result, self.i)        
    return self.result

  def PostOrderWalk(self, r, arr, i):
    if i != -1:
      self.PostOrderWalk(self.key[self.left[i]], arr, self.left[i])
      self.PostOrderWalk(self.key[self.right[i]], arr, self.right[i])
      arr.append(self.key[i])

  def postOrder(self):
    self.result = []
    self.i = 0
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.PostOrderWalk(self.key[self.i], self.result, self.i)            
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
