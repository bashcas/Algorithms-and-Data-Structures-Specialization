# Uses python3
import sys
import random

def partition3(a, l, r):
    pivot = a[l]
    j = l
    k = 0
    for i in range(l + 1, r + 1):
        if a[i] <= pivot:
            j += 1
            if a[j - 1] == pivot and j - 1 != l:
                a[j - k], a[j] = a[j], a[j - k]
                if j != i:
                    a[j - k], a[i] = a[i], a[j - k]
                if a[j - k] == pivot: k += 1
                continue
            if a[i] == pivot: k += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j - k] = a[j - k], a[l]
    return j - k, j
    

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    pivot = random.randint(l, r)
    a[l], a[pivot] = a[pivot], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)

def randomized_quick_sort_test(a, l, r):
    if l >= r:
        return
    pivot = random.randint(l, r)
    a[l], a[pivot] = a[pivot], a[l]
    m1 = partition2(a, l, r)
    randomized_quick_sort_test(a, l, m1 - 1)
    randomized_quick_sort_test(a, m1 + 1, r)

if __name__ == '__main__':
    # stress test
    # test = 1
    # failed = False
    # while not failed:
    #     nums = [random.randint(5, 10) for i in range(10)]
    #     print(len(nums))
    #     nums2 = [*nums]
    #     print(*nums)
    #     randomized_quick_sort_test(nums, 0, len(nums) - 1)
    #     randomized_quick_sort(nums2, 0, len(nums2) - 1)

        
    #     for i in range(len(nums)):
    #         if nums[i] == nums2[i]:
    #             pass
    #         else:
    #             print(f"Test {test} failed")
    #             print(f"nums: {nums}")
    #             print(f"num2: {nums2}")
    #             failed = True
    #             break
    #     print(f"Test {test} passed")
    #     test += 1

    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
