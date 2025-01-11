def f(number, even):
    # Convert the number to a string
    number_str = str(number)
    
    # Initialize the sum to 0
    digit_sum = 0

    # Loop through each digit in the string
    for digit in number_str:
        # Convert the digit back to an integer
        digit_int = int(digit)
        
        # Check if the digit is even or odd based on the 'even' parameter
        if even and digit_int % 2 == 0:
            digit_sum += digit_int  # Add the even digit to the sum
        elif not even and digit_int % 2 != 0:
            digit_sum += digit_int  # Add the odd digit to the sum

    # Return the final sum
    return digit_sum

# Sample usage
print(f(3124, True))   # Returns 6 (sum of 2 and 4)
print(f(3124, False))  # Returns 4 (sum of 3 and 1)
print(f(20576, False)) # Returns 12 (sum of 5 and 7)
print(f(20576, True))  # Returns 8 (sum of 2 and 6)
print(f(13115, True))  # Returns 0 (no even digits)