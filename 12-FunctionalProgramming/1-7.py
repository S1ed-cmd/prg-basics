is_even = lambda number: number % 2 == 0

number = int(input("Enter your number:"))

if  is_even(number):
    print(f"the number {number} is even")
else:
    print(f"the number {number} is odd")