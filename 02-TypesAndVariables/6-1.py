name = input('Enter your name:')   
surname = input('Enter your surname:')

characters_in_name = len(name)
characters_in_surname = len(surname)
characters_in_full_name = len(name +' '+  surname) 

print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {characters_in_surname} characters')
print(f'Your full name has {characters_in_full_name} characters')