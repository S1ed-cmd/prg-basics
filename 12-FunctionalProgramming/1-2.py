# takes two numbers from keyboard
n1 = float(input("Enter first number:"))
n2 = float(input("Enter second number:"))

# define an anonymous function
mean = lambda x,y: (x+y)/2


# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f"The arithmetic mean of {n1} and  {n2} is {mean}")