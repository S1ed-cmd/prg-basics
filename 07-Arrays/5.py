arrays = [8,2,5,1,9]

square_array = []
    
for i in arrays:
    square_array.append(i ** 2)



print("Array:", " ".join(map(str, arrays)))
print("Array:", " ".join(map(str, square_array)))
