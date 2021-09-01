def naive_GCD(a, b):
  gcd = 0
  for d in range(1, a+b+1):
    if a % d == 0 and b % d == 0:
      gcd = d
  return gcd

def euclid_GCD(a, b):
  if b == 0:
    return a
  remainder = a % b
  return euclid_GCD(b, remainder)
  
nums = input()
nums = nums.split()

result = euclid_GCD(int(nums[0]), int(nums[1]))
print(str(result))