import sys

def majority_element(A):
    dic = {}
    for n in A:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1
    for v in dic.values():
        if v > len(A) / 2:
            return 1
    return 0 

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    el = majority_element(data[1:])
    print(el)