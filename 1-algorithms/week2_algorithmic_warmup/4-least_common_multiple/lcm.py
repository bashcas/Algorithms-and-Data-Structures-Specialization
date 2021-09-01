def gcd(a, b) -> int:
  if b == 0:
    return a
  remainder = a % b
  return gcd(b, remainder)

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a*b

def lcm_fast(a, b) -> int:
    return (a * b) / gcd(a, b)

if __name__ == '__main__':
    tokens = input()
    tokens = tokens.split()
    tokens = list(map(lambda t: int(t), tokens))
    print(int(lcm_fast(tokens[0], tokens[1])))
    


