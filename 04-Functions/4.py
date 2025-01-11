def f(text, find):
    count = 0
    for letter in text:
        if letter.lower() == find.lower():
            count+=1
    return count



if __name__ == "__main__":
    print(f("You never get a second chance to make a first impression", "e"))
    print("You never get a second chance to make a first impression".count("e"))