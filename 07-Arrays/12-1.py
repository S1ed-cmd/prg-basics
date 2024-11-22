categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
max_expense_index = expenses.index(max(expenses))
most_expensive_category = categories[max_expense_index]
print(most_expensive_category)
print(max_expense_index)