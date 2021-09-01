# python3

import sys
import threading

def create_tree(n, parents):
    nodes = [[] for _ in range(n)]
    root = 0
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            nodes[parents[i]].append(i)
    return root, nodes

def compute_height(root, nodes):
    if len(nodes[root]) == 0:
        return 0
    max_height = 0    
    for i in range(len(nodes[root])):
        height = 1 + compute_height(nodes[root][i], nodes)
        if height > max_height: max_height = height
    return max_height

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    root, nodes = create_tree(n, parents)
    print(compute_height(root, nodes) + 1)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
