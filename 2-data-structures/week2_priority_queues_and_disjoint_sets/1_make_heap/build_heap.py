# python3

class MinHeap():
    def __init__(self, arr = []) -> None:
        self.heap = arr
        self.swaps = []

    def left_child(self, i):
        return 2 * i + 1
    def right_child(self, i):
        return 2 * i + 2

    def sift_down(self, i):
        min_index = i
        l = self.left_child(i)
        if l <= len(self.heap) - 1 and self.heap[l] < self.heap[min_index]:
            min_index = l
        r = self.right_child(i)
        if r <= len(self.heap) - 1 and self.heap[r] < self.heap[min_index]:
            min_index = r
        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.swaps.append([i, min_index])
            self.sift_down(min_index)

    def build_heap(self):
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.sift_down(i)

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    heap = MinHeap(data)
    heap.build_heap()
    print(len(heap.swaps))
    for i, j in heap.swaps:
        print(i, j)


if __name__ == "__main__":
    main()
