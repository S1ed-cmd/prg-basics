numbers = [2, 6, 4, 9, 7]


def stars(n):
    return "*" * n

for number in numbers:
    print(f"{number}:{stars(number)}")