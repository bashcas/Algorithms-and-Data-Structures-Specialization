class StackWithMax():
    def __init__(self):
        self.stack = []
        self.aux = []

    def Push(self, a):
        self.stack.append(a)
        if len(self.aux) == 0:
            self.aux.append(a)
        elif a >= self.aux[-1]:
            self.aux.append(a)

    def Pop(self):
        el = self.stack.pop()
        if self.aux[-1] == el:
            self.aux.pop()
        return el

    def Max(self):
        if len(self.aux) == 0:
            return -1
        return self.aux[-1]
    
    def Void(self):
        self.stack = []
        self.aux = []

class Queue():
    def __init__(self) -> None:
        self.input = StackWithMax()
        self.output = StackWithMax()

    def enqueue(self, a):
        self.input.Push(a)

    def dequeue(self):
        if len(self.output.stack) == 0:
            while len(self.input.stack) > 0:
                el = self.input.Pop()
                self.output.Push(el)
        return self.output.Pop()

    def max(self):
        return max(self.input.Max(), self.output.Max())

def max_sliding_window_naive(sequence: list, m: int):
    maximums = []
    window = Queue()
    for i in range(m):
        window.enqueue(sequence[i])
    maximums.append(window.max())

    for i in range(m, len(sequence)):
        window.dequeue()
        window.enqueue(sequence[i])
        maximums.append(window.max())
    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    print(*max_sliding_window_naive(input_sequence, window_size))


