student = {
   'name': 'John',

   'age': 22,
   'major': 'Computer Science'
}

# Accessing a value
print(student['name'])

# Adding a new key-value pair
student['grade'] = 'A'

# Modifying an existing value
student['age'] = 23

# Deleting a key-value pair
del student['major']
print(student)

fruits = {'apple': 15, 'banana': 18, 'orange': 2}

# Iterating over keys
for i  in fruits:
   print(i)

# Iterating over values
for n in fruits.values():
   print(n)

# Iterating over key-value pairs
for i, n in fruits.items():
   print(f"The count of {i} is {n}")

# Create a dictionary
person = {'name': 'Alice', 'age': 30}

# Check if a key exists
if 'name' in person:
   print("Name is present in the dictionary.")
else:
   print("Name is not present.")