names = [
    'James',
    'Emily',
    'William',
    'Olivia',
    'Benjamin',
    'Sophia',
    'Henry']

print("\nUnsorted list:")
print(names)

sorted_names = sorted(names, key=len)

print("\nSorted list:")
for name in sorted_names:
    print(name)
