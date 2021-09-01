# python3
import sys

class Database():
    def __init__(self, n, lines):
        self.n = n
        self.lines = [0] + lines
        self.rank = [0] * (n + 1)
        self.parent = list(range(0, n + 1))
        self.max = max(self.lines)

    def find(self, i):
        parents_to_update = []
        root = i
        while root != self.parent[root]:
            parents_to_update.append(self.parent[root])
            root = self.parent[root]
        for i in parents_to_update:
            self.parent[i] = root
        return root

    def merge(self, dst, src):
        src_root = self.find(src)
        dst_root = self.find(dst)

        if src_root == dst_root:
            return
        if self.rank[src_root] >= self.rank[dst_root]:
            self.parent[src_root] = dst_root
        else:
            self.parent[dst_root] = src_root
            if self.rank[src_root] == self.rank[dst_root]:
                self.rank[src_root] += 1

        self.lines[dst_root] += self.lines[src_root]
        self.lines[src_root] = 0

        if self.max < self.lines[dst_root]:
            self.max = self.lines[dst_root]

    def get_max_lines(self):
        return self.max

def main():
    n_tables, n_queries = map(int, sys.stdin.readline().split())
    counts = list(map(int, sys.stdin.readline().split()))
    assert len(counts) == n_tables
    db = Database(n_tables, counts)
    for i in range(n_queries):
        dst, src = map(int, sys.stdin.readline().split())
        db.merge(dst, src)
        print(db.get_max_lines())

if __name__ == "__main__":
    main()
