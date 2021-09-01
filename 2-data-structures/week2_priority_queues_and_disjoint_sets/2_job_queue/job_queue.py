# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

class Thread():
    def __init__(self, idx, free_at) -> None:
        self.idx = idx
        self.free_at = free_at

class MinHeap():
    def __init__(self, n) -> None:
        self.heap = [Thread(i, 0) for i in range(n)]

    def left_child(self, i):
        return 2 * i + 1
    def right_child(self, i):
        return 2 * i + 2

    def sift_down(self, i):
        min_index = i
        l = self.left_child(i)
        if l <= len(self.heap) - 1 and self.heap[l].free_at <= self.heap[min_index].free_at:
            if self.heap[l].free_at == self.heap[min_index].free_at:
                if self.heap[l].idx < self.heap[min_index].idx:
                    min_index = l
            else:
                min_index = l
        r = self.right_child(i)
        if r <= len(self.heap) - 1 and self.heap[r].free_at <= self.heap[min_index].free_at:
            if self.heap[r].free_at == self.heap[min_index].free_at:
                if self.heap[r].idx < self.heap[min_index].idx:
                    min_index = r
            else:
                min_index = r
        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.sift_down(min_index)

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    workers = MinHeap(n_workers)
    for job in jobs:
        worker = workers.heap[0]
        result.append(AssignedJob(worker.idx, worker.free_at))
        workers.heap[0].free_at += job
        workers.sift_down(0) 

    return result

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)