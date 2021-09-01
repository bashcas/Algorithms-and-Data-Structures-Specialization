# coins of value 1, 5 and 10
#returns total of coins
def change_by_coins(n: int) -> int:
    coins = n // 10 # 2
    remainder = n % 10 #
    coins += remainder // 5
    remainder = n % 5
    coins += remainder
    return coins

if __name__ == "__main__":
    n = int(input())
    print(int(change_by_coins(n)))