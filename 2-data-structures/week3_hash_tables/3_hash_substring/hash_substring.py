# python3
from random import randint

def rabin_karp(P, T):
    p = 1000000007
    x = randint(1, p - 1)
    result = []
    p_hash = poly_hash(P, p, x)
    H = precompute_hashes(T, P, p, x)
    for i in range(0, len(T) - len(P) + 1):
        if p_hash != H[i]:
            continue
        if P == "".join(T[i: len(P) + i]):
            result.append(i)
    return result

def poly_hash(S, p, x):
    hash = 0
    for c in reversed(S):
        hash = (hash * x + ord(c)) % p
    return hash

def precompute_hashes(T, P, p, x):
    H = [None] * (len(T) - len(P) + 1)
    last_substr = T[len(T) - len(P):len(T)]
    H[len(T) - len(P)] = poly_hash(last_substr, p, x)
    y = 1
    for i in range(1, len(P) + 1):
        y = (y * x) % p
    for i in reversed(range(len(T) - len(P))):
        pre_hash = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + len(P)]))
        #important to avoid too much collisions 
        while(pre_hash < 0):
            pre_hash += p
        H[i] = pre_hash % p
    return H

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

if __name__ == '__main__':
    print_occurrences(rabin_karp(*read_input()))

