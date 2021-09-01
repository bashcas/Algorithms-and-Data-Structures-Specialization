
def optimal_weight_without_repetitions(W, w):
    w = [0] + w
    items = len(w)
    capacity = W + 1
    
    optimal_weights = [[0 for _ in range(items)] for _ in range(capacity)]
    for i in range(len(optimal_weights)):
        print(optimal_weights[i])
    for i in range(1, items):
        for x in range(1, capacity):
            optimal_weights[x][i] = optimal_weights[x][i - 1]
            if w[i] <= x:
                opt = optimal_weights[x - w[i]][i - 1] + w[i]
                if optimal_weights[x][i] < opt:
                    optimal_weights[x][i] = opt

    return optimal_weights[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight_without_repetitions(W, w))
