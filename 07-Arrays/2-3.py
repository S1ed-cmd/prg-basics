monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
result = 0
# Use loop statements
for row in monthly_expenses:
    for item in row:
        result += item



# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',monthly_expenses[0][0],monthly_expenses[1][0],monthly_expenses[2][0],monthly_expenses[3][0])
print('Transport:',monthly_expenses[0][1],monthly_expenses[1][1],monthly_expenses[2][1],monthly_expenses[3][1])
print('Utilities:',...)
print('Week 1:',monthly_expenses[0])
print('Week 2:',monthly_expenses[1])
print('Week 3:',monthly_expenses[2])
print('Week 4:',monthly_expenses[3])
print('---------------')
print('TOTAL:',result)