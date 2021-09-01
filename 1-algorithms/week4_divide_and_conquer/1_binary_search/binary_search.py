import sys

def binary_search(A, low, high, value):
    if high < low:
        return - 1
    mid = int((high - low) / 2 + low)
    if A[mid] == value:
        return mid
    elif A[mid] > value:
        return binary_search(A, low, mid - 1, value)
    elif A[mid] < value:
        return binary_search(A, mid + 1, high, value)

if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    a.sort()
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, 0, len(a) - 1, x), end = ' ')

    