# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    numbers = [0, 1]
    for i in range(2, n + 1):
        numbers.append((numbers[i - 1] + numbers[i - 2]) % 10)
    return numbers[n]

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
