def f(detector):
 count = 0
 max_count = 0
 for i in detector:
   if i == "+":
     count += 1
   elif i == "-":
      count -= 1
   max_count = max(max_count, count) 

 return max_count >= 3

# Sample usage
print(f("+-+++-+---"))     # Output: True
print(f("+-+-+-+-"))       # Output: False
print(f("+-++-+--"))       # Output: False
print(f("+-++-++-+---"))   # Output: True