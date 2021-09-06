# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    result = []
    self.inOrderTraversal(0, result)       
    return result

  def inOrderTraversal(self, node: int, result: list):
    if self.left[node] == -1 and self.right[node] == -1:
      result.append(self.key[node])
      return
    elif self.left[node] == -1:
      result.append(self.key[node])
      self.inOrderTraversal(self.right[node], result)
    elif self.right[node] == -1:
      self.inOrderTraversal(self.left[node], result)
      result.append(self.key[node])
    else:
      self.inOrderTraversal(self.left[node], result)
      result.append(self.key[node])
      self.inOrderTraversal(self.right[node], result)

  def preOrder(self):
    result = []
    self.preOrderTraversal(0, result)
    return result
  
  def preOrderTraversal(self, node: int, result: list):
    result.append(self.key[node])
    if self.left[node] == -1 and self.right[node] == -1:
      return
    elif self.left[node] == -1:
      self.preOrderTraversal(self.right[node], result)
    elif self.right[node] == -1:
      self.preOrderTraversal(self.left[node], result)
    else:
      self.preOrderTraversal(self.left[node], result)
      self.preOrderTraversal(self.right[node], result)

  def postOrder(self):
    result = []
    self.postOrderTraversal(0, result)
    return result
  
  def postOrderTraversal(self, node: int, result: list):
    if self.left[node] == -1 and self.right[node] == -1:
      result.append(self.key[node])
      return
    elif self.left[node] == -1:
      self.postOrderTraversal(self.right[node], result)
    elif self.right[node] == -1:
      self.postOrderTraversal(self.left[node], result)
    else:
      self.postOrderTraversal(self.left[node], result)
      self.postOrderTraversal(self.right[node], result)

    result.append(self.key[node])


def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
