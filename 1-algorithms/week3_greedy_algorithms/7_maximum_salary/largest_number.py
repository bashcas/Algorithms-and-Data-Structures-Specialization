#Uses python3

import sys

def is_greater_or_equal(a: str, b: str):
    if a + b > b + a:
        return True
    else:
        return False

def largest_number(numbers: list):
    nums = [*numbers]
    answer = ""
    while len(nums) > 0:
        maxDigit = "0"
        for n in range(len(nums)):
            if is_greater_or_equal(nums[n], nums[int(maxDigit)]):
                maxDigit = str(n)
        answer += nums[int(maxDigit)]
        nums.pop(int(maxDigit))

    return answer

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

    
