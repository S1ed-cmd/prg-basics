num = [ -15, 8, -31, 47, -2, 19.]


minimum = num[0]
maximum = num[0]


for i in num:
    if i > maximum:
     maximum = i
    if i < minimum:
     minimum = i



print("Maximum number:", maximum)
print("Minimum number:", minimum)