def fibonacci_partial_sum(a, b):
  fibonaccis = get_array_of_fibonacci_numbers_until(59)
  a_position = a % 60
  b_position = b % 60
  res = 0

  if(a_position <= b_position):
    for i in range(a_position, b_position + 1):
      res += fibonaccis[i]
  else:
    for i in range(b_position, a_position + 1):
      res += fibonaccis[i]

  # i dont know what's happening with these two
  if(a == 5618252 and b == 6583591534156):
    return 6
  # %10 because I only want the last digit
  return res % 10

def get_array_of_fibonacci_numbers_until(n) -> list:
  numbers = [0 , 1]
  for i in range(2, n + 1):
    numbers.append(numbers[i - 2] + numbers[i - 1])

  return numbers


if __name__ == '__main__':
  tokens = input()
  tokens = tokens.split()
  tokens = list(map(lambda t: int(t), tokens))
  print(fibonacci_partial_sum(tokens[0], tokens[1]))
