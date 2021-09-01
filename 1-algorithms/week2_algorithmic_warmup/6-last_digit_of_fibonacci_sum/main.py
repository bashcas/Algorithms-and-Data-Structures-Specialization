
def get_array_of_fibonacci_numbers_until(n) -> list:
  numbers = [0 , 1]
  for i in range(2, n + 1):
    numbers.append(numbers[i - 2] + numbers[i - 1])

  return numbers

def fibonacci_sum_fast(n):
  #60 because last_digits are period every 60 steps
  fibonaccis = get_array_of_fibonacci_numbers_until(60)
  last_digits = []
  
  sum = 0
  for fib in fibonaccis:
    sum += fib
    last_digits.append(sum % 10)

  number_position = n % 60

  return last_digits[number_position]

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_fast(n))