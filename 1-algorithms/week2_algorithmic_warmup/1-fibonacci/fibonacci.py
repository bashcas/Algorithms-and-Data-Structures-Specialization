def recursive_fibonacci(n):
  if(n <= 1):
    return n

  return recursive_fibonacci(n - 2) + recursive_fibonacci(n - 1)

def fast_fibonacci(n):
  numbers = [0, 1]
  for i in range(2, n + 1):
    numbers.append(numbers[i - 2] + numbers[i - 1])

  return numbers[n]


fibonacci = int(input())
print(fast_fibonacci(fibonacci))
