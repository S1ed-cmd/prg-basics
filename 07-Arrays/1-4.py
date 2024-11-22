##number of elements
#irst value
#second value
#last value
#last but one value (do not use negative index values)
#sum of the first and last value
#middle value
#all array values separated by a single space (use a loop statement)
###

arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Last value', arr[-2])

print('sum of arrays', arr[0] + arr[-1])
mid_value = len(arr) // 2
print('middle value', arr[mid_value])

print("All values:", end=" ")
for value in arr:
     print(value, end=" ")
print()  