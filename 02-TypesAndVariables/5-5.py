price = float(input( 'Enter a price:'))
discount = float(input('Enter a discount:'))
percent_of_discount = price * discount / 100
price_with_discount = price - percent_of_discount

reduction = price - price_with_discount
print(f'Price with discount is {price_with_discount}')
print(f'Redurection is {reduction}')