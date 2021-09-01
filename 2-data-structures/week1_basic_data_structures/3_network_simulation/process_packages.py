# python3

from collections import namedtuple
import random
import time

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process_with_filter(self, request):

        #filter
        self.finish_time = list(filter(lambda time: time > request.arrived_at, self.finish_time))

        if len(self.finish_time) >= self.size:
            return Response(True, -1)
        elif len(self.finish_time) == 0:
            finish_at = request.arrived_at + request.time_to_process
            self.finish_time.append(finish_at)
            return Response(False, request.arrived_at)
        else:
            finish_at = request.time_to_process + self.finish_time[-1]
            self.finish_time.append(finish_at)
            return Response(False, finish_at - request.time_to_process)

    def process(self, request):

        #filter
        occurrence = len(self.finish_time) > 0
        while occurrence:
            if len(self.finish_time) == 0: break
            if self.finish_time[0] > request.arrived_at:
                occurrence = False
            else:
                self.finish_time.pop(0)

        if len(self.finish_time) >= self.size:
            return Response(True, -1)
        elif len(self.finish_time) == 0:
            finish_at = request.arrived_at + request.time_to_process
            self.finish_time.append(finish_at)
            return Response(False, request.arrived_at)
        else:
            finish_at = request.time_to_process + self.finish_time[-1]
            self.finish_time.append(finish_at)
            return Response(False, finish_at - request.time_to_process)

def process_requests_with_filter(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process_with_filter(request))
    return responses

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses




def main():
    #stress test
    buffer_size = 1000
    buffer = Buffer(buffer_size)
    requests = []
    j = random.randint(80, 150)
    l = 0
    k = 0
    for _ in range(100000):
        requests.append(Request(k, random.randint(100, 1000)))
        if l == j:
            j = random.randint(80, 150)
            k += 1
            l = 0
        l += 1
    start_time = time.time()
    responses = process_requests(requests, buffer)
    print(f"without filter: {time.time() - start_time} seconds")
    buffer.finish_time = []
    start_time = time.time()
    responses = process_requests_with_filter(requests, buffer)
    print(f"with filter: {time.time() - start_time} seconds")
   

        




    # buffer_size, n_requests = map(int, input().split())
    # requests = []
    # for _ in range(n_requests):
    #     arrived_at, time_to_process = map(int, input().split())
    #     requests.append(Request(arrived_at, time_to_process))

    # buffer = Buffer(buffer_size)
    # responses = process_requests(requests, buffer)

    # for response in responses:
    #     print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
