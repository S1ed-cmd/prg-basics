distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input ('Enter your fuel consuption for 100km: '))
total_fuel_consumption = (fuel_consumption / 100) * distance
total_cost = total_fuel_consumption * fuel_price
print(f'Total fuel consumption: {total_fuel_consumption}, liters')
print(f'Total cost of transportation: ${total_cost}')