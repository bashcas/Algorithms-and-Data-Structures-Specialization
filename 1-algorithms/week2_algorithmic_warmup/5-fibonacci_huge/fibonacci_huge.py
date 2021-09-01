def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci(n):
    numbers = [0, 1]
    for i in range(2, n + 1):
        numbers.append(numbers[i - 2] + numbers[i - 1])

    return numbers[n]

def get_array_of_fibonacci_numbers_until(n) -> list:
  numbers = [0 , 1]
  for i in range(2, n + 1):
    numbers.append(numbers[i - 2] + numbers[i - 1])
  
  return numbers

def get_pisano_period(m):
    fibonaccis = get_array_of_fibonacci_numbers_until(5000)
    sequence = [0, 1]
    for i in range(2, len(fibonaccis)):
        mod = fibonaccis[i] % m
        following_mod = fibonaccis[i + 1] % m
        if(mod == 0 and following_mod == 1):
          break

        sequence.append(mod)
    return len(sequence)


def get_fibonacci_huge_fast(nth_fibonacci, m):
    remainder = nth_fibonacci % get_pisano_period(m)
    fib = get_fibonacci(remainder)
    return fib % m

if __name__ == '__main__':
    tokens = input()
    tokens = tokens.split()
    tokens = list(map(lambda t: int(t), tokens))
    print(int(get_fibonacci_huge_fast(tokens[0], tokens[1])))
