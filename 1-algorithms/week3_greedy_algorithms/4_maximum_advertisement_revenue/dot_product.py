import random
import time

def max_dot_product_naive(ad_profit: list, slot_average_number_of_clicks: list) -> int:
    res = 0
    best_ad = 0
    best_slot = 0

    while len(ad_profit) > 0:
        for i in range(len(ad_profit)):
            if ad_profit[i] > ad_profit[best_ad]:
                best_ad = i

        for i in range(len(slot_average_number_of_clicks)):
            if slot_average_number_of_clicks[i] > slot_average_number_of_clicks[best_slot]:
                best_slot = i

        res += slot_average_number_of_clicks[best_slot] * ad_profit[best_ad]
        ad_profit.pop(best_ad)
        slot_average_number_of_clicks.pop(best_slot)
        best_ad = 0
        best_slot = 0

    return res

def max_dot_product(ad_profit: list, slot_average_number_of_clicks: list) -> int:
    res = 0
    ad_profit.sort(reverse=True)
    slot_average_number_of_clicks.sort(reverse=True)
    for i in range(len(ad_profit)):
        res += ad_profit[i] * slot_average_number_of_clicks[i]
    return res

if __name__ == '__main__':
    #stress test
    while True:
        n = random.randint(1, 10e3) + 2000
        print(n)
        ad_profit = [random.randint(-10e5, 10e5) for _ in range(n)]
        slots = [random.randint(-10e5, 10e5) for _ in range(n)]
        start = time.time()
        max_dot_product(ad_profit, slots)
        print(f"{time.time() - start} seconds")
        start = time.time()
        max_dot_product_naive(ad_profit, slots)
        print(f"{time.time() - start} seconds")


    n = int(input())
    ad_profit = list(map(lambda a: int(a), input().split()))
    slot_average_number_of_clicks = list(map(lambda a: int(a), input().split()))
    print(max_dot_product(ad_profit, slot_average_number_of_clicks))
    # print(max_dot_product_naive(ad_profit, slot_average_number_of_clicks))
    
    
