SWIFT = input('Enter your SWIFt code:')
print(f'Your bank code is:', {SWIFT[0:4]})
print('your country code', {SWIFT[4:6]})
print( 'location code', {SWIFT[6:8]})
print( 'branch code', {SWIFT[8:11]})