#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
positive_infinity = 4294967296
negative_infinity = -4294967296
# tree[0] = 0th node
# tree[1] = 1th node
# tree[n] = nth node
# node[0] = key 
# node[1] = left child index 
# node[2] = right child index 
def IsBinarySearchTree(tree):
  if len(tree) == 0:
    return True
  return IsBinarySearchTreeAux(tree, negative_infinity, positive_infinity, 0)

def IsBinarySearchTreeAux(tree, mini, maxi, node):

  if tree[node][0] < mini or tree[node][0] > maxi:
    return False

  if tree[node][1] == -1 and tree[node][2] == -1:
    return True

  if tree[node][1] == -1:
    return IsBinarySearchTreeAux(tree, tree[node][0], maxi, tree[node][2])
  
  if tree[node][2] == -1:
    return IsBinarySearchTreeAux(tree, mini, tree[node][0] - 1, tree[node][1])
  
  return IsBinarySearchTreeAux(tree, mini, tree[node][0] - 1, tree[node][1]) and IsBinarySearchTreeAux(tree, tree[node][0], maxi, tree[node][2])


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
