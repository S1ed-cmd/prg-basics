def f(amount_to_pay):
    # Initialize the count of coins
    coin_count = 0
    
    # Use the largest coin denomination first (5 PLN)
    coin_count += amount_to_pay // 5
    amount_to_pay %= 5

    # Use the next largest coin denomination (2 PLN)
    coin_count += amount_to_pay // 2
    amount_to_pay %= 2

    # Use the smallest coin denomination (1 PLN)
    coin_count += amount_to_pay // 1  # amount_to_pay is either 0 or 1 here

    return coin_count

# Sample usage
print(f(23))  # Returns 6 (4x5 PLN + 1x2 PLN + 1x1 PLN)
print(f(8))   # Returns 3 (1x5 PLN + 1x2 PLN + 1x1 PLN)
print(f(2))   # Returns 1 (1x2 PLN)
print(f(0))   # Returns 0 (no coins needed)