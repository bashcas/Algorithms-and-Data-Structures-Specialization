# Uses python3
import sys

# Just a reference 
def merge(A: list, B: list):
    D = []
    while len(A) > 0 and len(B) > 0:
        a = A[0]
        b = B[0]
        if a <= b:
            D.append(a)
            A.pop(0)
        else:
            D.append(b)
            B.pop(0)
    D += A
    D += B
    return D

# Just a reference 
def merge_sort(A):
    if len(A) == 1:
        return A
    m = len(A) // 2
    B = merge_sort(A[0: m])
    C = merge_sort(A[m: len(A)])
    D = merge(B, C)
    return D

def merge_number_of_inversions(A: list, B: list):
    inversions = 0
    D = []
    while len(A) > 0 and len(B) > 0:
        a = A[0]
        b = B[0]
        if a <= b:
            D.append(a)
            A.pop(0)
        else:
            inversions += len(A)
            D.append(b)
            B.pop(0)
    D += A
    D += B
    return inversions, D

def get_number_of_inversions(A):
    number_of_inv = 0
    if len(A) == 1:
        return A, number_of_inv
    m = len(A) // 2
    B, number_of_invB = get_number_of_inversions(A[0: m])
    C, number_of_invC = get_number_of_inversions(A[m: len(A)])
    number_of_inv += number_of_invB + number_of_invC

    number_of_invD, D = merge_number_of_inversions(B, C)
    number_of_inv += number_of_invD
    return D, number_of_inv

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    res = get_number_of_inversions(a)
    print(res[1])
