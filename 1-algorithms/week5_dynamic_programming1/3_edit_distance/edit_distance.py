# Uses python3
def edit_distance(a, b):
    matrix = [[] for _ in range(len(b) + 1)]
    s = list(a)
    s.insert(0, "")
    t = list(b)
    t.insert(0, "")
    for i in range(1, len(matrix)):
        matrix[i].append(i)
    for i in range(len(a) + 1):
        matrix[0].append(i)

    for i in range(1, len(b) + 1):
        for j in range(1, len(a) + 1):
            insertion = matrix[i - 1][j] + 1
            deletion = matrix[i][j - 1] + 1
            mismatch = matrix[i - 1][j - 1] + 1
            match = matrix[i - 1][j - 1]
            if s[j] == t[i]:
                matrix[i].insert(j, min(insertion, deletion, match))
            else:
                matrix[i].insert(j, min(insertion, deletion, mismatch))
    return matrix[len(matrix) - 1][len(a)]

if __name__ == "__main__":
    res = edit_distance(input(), input())
    print(res)
