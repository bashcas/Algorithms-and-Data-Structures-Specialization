# python3
class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]

class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[] for _ in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            if len(self.elems[query.ind]) == 0:
                print("")
            else:
                print(*reversed(self.elems[query.ind]))
        else:
            if query.type == 'find':
                ind = self._hash_func(query.s)
                for s in self.elems[ind]:
                    if s == query.s:
                        print("yes")
                        return True
                print("no")
                return False
            elif query.type == 'add':
                ind = self._hash_func(query.s)
                for s in self.elems[ind]:
                    if s == query.s:
                        return
                self.elems[ind].append(query.s)
            else:
                ind = self._hash_func(query.s)
                for i, str in enumerate(self.elems[ind]):
                    if str == query.s:
                        self.elems[ind].pop(i)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
