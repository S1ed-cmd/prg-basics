import random
comp_dice = random.randint(1,6)
player = float(input('Try to guess which number was rolled: '))
win = player == comp_dice
print(f'DId you won? ', (win))