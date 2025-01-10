initials = lambda name, surname: name[0].upper() + surname[0].upper()
name = input("Enter you name:")
surname = input("enter your surname:")
print(f"your Initials: {initials(name,surname)}")