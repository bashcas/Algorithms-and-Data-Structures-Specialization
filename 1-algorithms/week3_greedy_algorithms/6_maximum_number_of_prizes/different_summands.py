# Uses python3
import sys

def optimal_summands_naive(n):
    summands = []
    map = {}
    aux = 1
    times = 0
    for i in range(1, n + 1):
        if times == aux + 1:
            times = 0
            aux += 1
        map[i] = aux
        times += 1
    summands = [i for i in range(1, map[n] + 1)]
    summands.pop()
    sum = 0
    for number in summands:
        sum += number
    summands.append(n - sum)
    return summands

def optimal_summands(n):
    summands = []
    sum = 0
    i = 1
    while sum < n:
        if sum + i > n:
            sum -= i - 1
            summands.pop()
            i = n - sum
            sum += i
            summands.append(i)
            break

        summands.append(i)
        sum += i
        i += 1

    return summands
        


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
    
