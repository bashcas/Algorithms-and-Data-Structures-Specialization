import random
import time
def get_optimal_value(capacity, weights: list, values):
    value = 0.
    items_arranged= []

    #arrange itemscl
    for i in range(len(weights)):
        items_arranged.append({"total_weight": weights[i], "total_value": values[i],})

    items_arranged.sort(key=lambda obj: obj["total_value"] / obj["total_weight"], reverse=True)

    #see how much of an item can fit into the knapsack
    while(len(items_arranged) > 0 and capacity > 0):
        item = items_arranged[0]

        #amount of item that fits
        amount_of_item = capacity / item["total_weight"]
        if item["total_value"] == 0:
            items_arranged.pop(0)
            continue
        elif amount_of_item >= 1:
            value += item["total_value"]
            capacity -= item["total_weight"]
        elif amount_of_item < 1:
            value += item["total_value"] * amount_of_item
            capacity -= item["total_weight"] * amount_of_item
        items_arranged.pop(0)
    #update data
    return value

def get_optimal_value_naive(capacity, weights: list, values):
    value = 0.
    while len(weights) > 0 and capacity > 0:
        best = 0
        for i in range(len(weights)):
            if values[i] / weights[i] >= values[best] / weights[best]:
                best = i

        amount: float = capacity / weights[best]
        if amount >= 1:
            capacity -= weights[best]
            value += values[best]
            weights.pop(best)
            values.pop(best)
            continue
        else:
            capacity -= amount * weights[best]
            value += amount * values[best]
            weights.pop(best)
            values.pop(best)
    
    return value



if __name__ == "__main__":
    # counter = 1
    # while(True):
    #     items_quantity = random.randint(1, 10e5)
    #     capacity = random.randint(0, 1000) + 1
    #     weights = [random.randint(0, 10e4)+1 for i in range(items_quantity)]
    #     values = [random.randint(0, 10e4)+1 for i in range(items_quantity)]
    #     weights2 = weights[:]
    #     values2 = values[:]
    #     capacity2 = capacity

    #     time_start = time.time()
    #     res = get_optimal_value(capacity, weights, values)
    #     print(f"time-optimal: {time.time() - time_start}")
    #     time_start = time.time()
    #     res2 = get_optimal_value_naive(capacity2, weights2, values2)
    #     print(f"time-naive: {time.time() - time_start}")
        # try:
        #     assert abs(res - res2) <= 10e-3
        #     print(f"test #{counter} passed")
        #     counter += 1
        # except(AssertionError):
        #     print(f"test #{counter} failed")
        #     print(f"got {res} and {res2}")
        #     print(f"these were your parameters:")
        #     print(f"quantity: {items_quantity}")
        #     print(f"capacity: {capacity}")
        #     break
        
    data = input()
    data = data.split()
    data = list(map(lambda n: int(n), data))
    number_of_items = data[0]
    knapsack_capacity = data[1]
    weights = []
    values = []
    for _ in range(number_of_items):
        item = input()
        item = item.split()
        values.append(int(item[0]))
        weights.append(int(item[1]))
    
    opt_value = get_optimal_value(knapsack_capacity, weights, values)
    print("{:.10f}".format(opt_value))
