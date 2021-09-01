# change for 1, 3 and 4 coin denominations
coins = [1, 3, 4]
def dp_change(money):
    min_num_coins = {0: 0}
    for m in range(1, money + 1):
        min_num_coins[m] = float("inf")
        for c in coins:
            if m >= c:
                num_coins = min_num_coins[m - c] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins

    return min_num_coins[money]

if __name__ == '__main__':
    m = int(input())
    print(dp_change(m))
