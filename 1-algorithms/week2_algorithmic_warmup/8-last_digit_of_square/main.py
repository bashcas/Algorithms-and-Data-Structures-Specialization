def fibonacci_square_sum(n):
  numbers = get_array_of_fibonacci_numbers_until(29)
  squares = list(map(lambda num: num**2, numbers))
  num_pos = n % 30
  sum = 0
  for i in range(0, num_pos + 1):
    sum+= squares[i]
 
  return sum % 10

def get_array_of_fibonacci_numbers_until(n) -> list:
  numbers = [0 , 1]
  for i in range(2, n + 1):
    numbers.append(numbers[i - 2] + numbers[i - 1])

  return numbers

if __name__ == "__main__":
  n = int(input())
  print(fibonacci_square_sum(n))