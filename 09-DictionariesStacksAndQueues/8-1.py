



#prints the total value of the products after the discount
price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
#prints a list of products and their prices before the discount
for a,b in price_list.items():
    print(f"{a}:{b}")
#prints the total value of the products before the discount
total_sum = sum(price_list.values())
print(total_sum)
#modifies the price list according to the discount (round prices to two decimal places)
discounted_price_list = {round(b * 0.9, 2) for a,b in price_list.items()}
totla_value = sum(discounted_price_list())
#prints a list of products and their prices after the 10% discount
print("Product       Price After Discount")
for a, b in discounted_price_list.items():
    print(f"{a:12} ${b:.2f}")

# Print the total value
print(f"\nTotal value of products after discount: ${totla_value:.2f}")